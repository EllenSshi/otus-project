import allure
from pages.BasePage import BasePage
from pages.locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage, LoginPageLocators):
    path = '/login'

    @allure.step("Log in")
    def login(self, username, password):
        self._input(self.USER_INPUT, username)
        try:
            self._click(self.LOGIN_ATLASSIAN_BTN)
        except NoSuchElementException:
            self._click(self.LOGIN_ATLASSIAN_BTN2)
        self._input(self.PASSWORD_INPUT, password)
        self._click(self.LOGIN_BTN)

    @allure.step("Verify if error message is present")
    def verify_login_error_msg(self):
        self._wait_for_visibility(self.LOGIN_ERROR_MSG)
