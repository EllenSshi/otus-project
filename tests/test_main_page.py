import allure
from pages.AllBoardsPage import AllBoardsPage
from pages.AllTemplatesPage import AllTemplatesPage
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from settings.credentials import USERNAME, PASSWORD


@allure.severity(allure.severity_level.MINOR)
@allure.feature("Go to the other page")
@allure.story("Go to Templates page")
@allure.title("From Main page go to Templates page")
def test_user_can_go_to_templates(browser):
    main_page = login_and_go_to_main_page(browser)
    main_page.go_to_templates()
    all_templates_page = AllTemplatesPage(browser)
    assert all_templates_page.verify_page()


def login_and_go_to_main_page(browser):
    LoginPage(browser).open().login(USERNAME, PASSWORD)
    all_boards_page = AllBoardsPage(browser)
    all_boards_page.go_to_main_page()
    return MainPage(browser)
