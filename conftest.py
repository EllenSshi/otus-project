import allure
import datetime
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Which browser to use for running tests"
    )
    parser.addoption(
        "--wait",
        default=60,
        type=int,
        help="Implicity wait for browser"
    )
    parser.addoption(
        "--executor",
        required=False
    )


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    wait = request.config.getoption("--wait")
    executor = request.config.getoption("--executor")
    if browser_name == "chrome":
        options = ChromeOptions()
        options.headless = True
        if not executor:
            browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.headless = True
        if not executor:
            browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("Undefined --browser_name. Should be 'chrome' or 'firefox'")

    if executor:
        browser = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
                                   desired_capabilities={
                                       "browserName": browser_name,
                                       "enableVnc": False,
                                       "enableVideo": False,
                                       "enableLog": True
                                   },
                                   options=options)

    browser = EventFiringWebDriver(browser, MyListener())
    browser.implicitly_wait(wait)
    yield browser
    browser.quit()


class MyListener(AbstractEventListener):
    def on_exception(self, exception, driver):
        now = datetime.datetime.now()
        allure.attach(name=driver.name + ' ' + str(now),
                      body=driver.get_screenshot_as_png(),
                      attachment_type=allure.attachment_type.PNG)
