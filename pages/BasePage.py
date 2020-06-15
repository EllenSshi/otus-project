import allure
from abc import abstractmethod
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
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

    def __element(self, selector: tuple, index: int = None):
        if index:
            return self.driver.find_elements(*selector)[index]
        else:
            return self.driver.find_element(*selector)

    def _elements(self, selector: tuple):
        return self.driver.find_elements(*selector)

    def _input(self, selector, value, index=None):
        with allure.step(f"Input into {selector} value '{value}'"):
            element = self.__element(selector, index)
            element.clear()
            element.send_keys(value)

    def _click(self, selector, index=None):
        with allure.step(f"Click on {selector}"):
            # ActionChains(self.driver).move_to_element(self.__element(selector, index)).click().perform()
            self.__element(selector, index).click()

    def _move_to_element(self, selector, index=None):
        ActionChains(self.driver).move_to_element(self.__element(selector, index).wrapped_element).click().perform()

    def _wait_for_visibility(self, selector, index=None, wait=20):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self.__element(selector, index)))

    def _get_element_text(self, selector, index=None):
        element = self.__element(selector, index)
        return element.get_attribute("value")

    def _get_element_attribute(self, element: WebElement, attribute: str):
        return element.get_attribute(attribute)

    def _get_element_property(self, element_property: str, selector=None, element: WebElement = None, index=None):
        if selector:
            element = self.__element(selector, index)
        return element.get_property(element_property)

    @allure.step("Check if admin logged in admin part")
    def verify_user_logged_in(self):
        try:
            self._wait_for_visibility(self.USER_BTN)
        except NoSuchElementException as e:
            raise AssertionError(e.msg)
