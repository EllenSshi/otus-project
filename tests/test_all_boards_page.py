import allure
import random
from pages.AllBoardsPage import AllBoardsPage
from pages.BoardPage import BoardPage
from pages.LoginPage import LoginPage
from settings.credentials import USERNAME, PASSWORD


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Create Board")
@allure.story("Create board from boards page")
@allure.title("Create private board")
def test_create_private_board(browser):
    board_name = f"Private board {random.randint(1,99)}"
    all_boards_page = login_and_create_private_board(browser, board_name)
    assert all_boards_page.verify_board_presence(board_name)


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Open Board")
@allure.story("Open board from boards page")
@allure.title("Open private board")
def test_open_board_by_name(browser):
    board_name = f"Private board {random.randint(1,99)}"
    all_boards_page = login_and_create_private_board(browser, board_name)
    all_boards_page.go_to_board(board_name)
    board_page = BoardPage(browser)
    assert board_page.get_board_name() == board_name


def login_and_create_private_board(browser, board_name):
    LoginPage(browser).open().login(USERNAME, PASSWORD)
    all_boards_page = AllBoardsPage(browser)
    all_boards_page.create_private_board(board_name)
    all_boards_page.open()
    return all_boards_page
