import allure
import random
from pages.AllBoardsPage import AllBoardsPage
from pages.AllTemplatesPage import AllTemplatesPage
from pages.TemplatePage import TemplatePage
from pages.BoardPage import BoardPage
from pages.LoginPage import LoginPage
from settings.credentials import USERNAME, PASSWORD


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Create Board")
@allure.story("Create board from template")
@allure.title("Create private board 'Reading list new' from template 'Reading list'")
def test_create_board_from_tmpl(browser):
    LoginPage(browser).open().login(USERNAME, PASSWORD)
    all_boards_page = AllBoardsPage(browser)
    all_boards_page.go_to_templates()
    all_templates_page = AllTemplatesPage(browser)
    all_templates_page.go_to_reading_list_template()
    template_page = TemplatePage(browser)
    board_from_tmpl_name = f"Board from template {random.randint(1, 99)}"
    template_page.create_board_from_tmpl(board_from_tmpl_name)
    all_boards_page.open()
    assert all_boards_page.verify_board_presence(board_from_tmpl_name)
