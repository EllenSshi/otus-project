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


@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Log out")
@allure.story("Valid log out")
@allure.title("Log out by valid user")
def test_log_out(browser):
    login_page = LoginPage(browser)
    login_page.open() \
        .login(USERNAME, PASSWORD)
    base_page = BasePage(browser)
    base_page.logout()
    base_page.verify_user_logged_out()


@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Log out")
@allure.story("Inalid log out")
@allure.title("Invalid log out on purpose for red test")
def test_failed_log_out(browser):
    login_page = LoginPage(browser)
    login_page.open() \
        .login(USERNAME, PASSWORD)
    base_page = BasePage(browser)
    base_page.verify_user_logged_out()
