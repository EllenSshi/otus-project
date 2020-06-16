import allure
from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from settings.credentials import USERNAME, PASSWORD


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Authorization")
@allure.story("Valid authorization")
@allure.title("Authorization as existent user")
def test_login(browser):
    login_page = LoginPage(browser)
    login_page.open()\
        .login(USERNAME, PASSWORD)
    base_page = BasePage(browser)
    base_page.verify_user_logged_in()


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Authorization")
@allure.story("Invalid authorization")
@allure.title("Authorization as nonexistent user")
def test_failed_login(browser):
    password = '1'
    login_page = LoginPage(browser)
    login_page.open() \
        .login(USERNAME, password)
    login_page.verify_login_error_msg()
