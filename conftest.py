import allure
import datetime
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
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
        default=20,
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
    options = None
    browser_profile = None
    if browser_name == "chrome":
        options = ChromeOptions()
        options.headless = False
        if not executor:
            browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.headless = False
        # browser_profile = webdriver.FirefoxProfile()
        if not executor:
            browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("Undefined --browser_name. Should be 'chrome' or 'firefox'")

    if executor:
        browser = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
                                   desired_capabilities={
                                       "browserName": browser_name,
                                       "enableVnc": True,
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
        # scr_name = driver.name + ' ' + str(now)
        # scr_body = driver.get_screenshot_as_png()
        # driver.save_screenshot(f'tests/screenshots/{scr_name}.png')
        allure.attach(name=driver.name + ' ' + str(now),
                      body=driver.get_screenshot_as_png(),
                      attachment_type=allure.attachment_type.PNG)
