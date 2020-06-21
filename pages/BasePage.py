import allure
from abc import abstractmethod
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from .locators import BasePageLocators


class BasePage(BasePageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://trello.com'

    @property
    @abstractmethod
    def path(self):
        return self.path

    @property
    def url(self):
        return self.base_url + self.path

    def open(self):
        with allure.step(f"Go to {self.url}"):
            self.driver.get(self.url)
            return self

    def __element(self, selector: tuple):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(selector))

    def _elements(self, selector: tuple):
        return self.driver.find_elements(*selector)

    def _input(self, selector, value, ):
        with allure.step(f"Input into {selector} value '{value}'"):
            element = self.__element(selector)
            element.clear()
            element.send_keys(value)

    def _click(self, selector):
        with allure.step(f"Click on {selector}"):
            self.__element(selector).click()
            # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(selector)).click()

    def _get_element_attribute(self, element: WebElement, attribute: str):
        return element.get_attribute(attribute)

    def _get_element_property(self, element_property: str, selector=None, element: WebElement = None):
        if selector:
            element = self.__element(selector)
        return element.get_property(element_property)

    def _get_element_text(self, selector):
        return self._get_element_attribute(self.__element(selector), "value")

    def _move_to_element(self, selector):
        ActionChains(self.driver).move_to_element(self.__element(selector).wrapped_element).click().perform()

    def _wait_for_visibility(self, selector, wait=20):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self.__element(selector)))

    @allure.step("Get current url")
    def get_current_url(self):
        return self.driver.current_url

    def verify_url(self, expected_url):
        return WebDriverWait(self.driver, 5).until(EC.url_to_be(expected_url))

    @allure.step("Log out")
    def logout(self):
        self._click(self.USER_BTN)
        self._click(self.LOGOUT_BTN)

    @allure.step("Verify if user logged in")
    def verify_user_logged_in(self):
        try:
            self._wait_for_visibility(self.USER_BTN)
        except TimeoutException as e:
            raise AssertionError(e.msg)

    @allure.step("Verify if user logged out")
    def verify_user_logged_out(self):
        try:
            self._wait_for_visibility(self.MAIN_LOGIN_BTN)
        except TimeoutException as e:
            raise AssertionError(e.msg)
