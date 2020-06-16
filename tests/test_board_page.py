import allure
import random
from pages.AllBoardsPage import AllBoardsPage
from pages.BoardPage import BoardPage
from pages.LoginPage import LoginPage
from settings.credentials import USERNAME, PASSWORD


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Edit Board")
@allure.story("Edit private board description")
@allure.title("Add private board first description")
def test_add_private_board_first_description(browser):
    board_name = f"Private board {random.randint(1, 99)}"
    board_page = login_and_create_private_board(browser, board_name)
    description = "98t"
    board_page.add_first_description(description)
    assert board_page.get_board_description() == description


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Add list on board")
@allure.story("Add list on private board")
@allure.title("Add list on private board")
def test_add_list(browser):
    board_name = f"Private board {random.randint(1, 99)}"
    board_page = login_and_create_private_board(browser, board_name)
    list_name = f"new list {random.randint(1, 99)}"
    board_page.add_list(list_name)
    assert board_page.verify_list_presence(list_name)


def login_and_create_private_board(browser, board_name):
    LoginPage(browser).open().login(USERNAME, PASSWORD)
    all_boards_page = AllBoardsPage(browser)
    all_boards_page.create_private_board(board_name)
    return BoardPage(browser)
