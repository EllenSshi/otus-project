import allure
import random
from pages.AllBoardsPage import AllBoardsPage
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from settings.credentials import USERNAME, PASSWORD


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Create Board")
@allure.story("Create board from main page")
@allure.title("Create private board")
def test_create_private_board(browser):
    board_name = f"Private board {random.randint(1, 99)}"
    all_boards_page = login_and_create_private_board(browser, board_name)
    assert all_boards_page.verify_board_presence(board_name)


def login_and_create_private_board(browser, board_name):
    LoginPage(browser).open().login(USERNAME, PASSWORD)
    all_boards_page = AllBoardsPage(browser)
    all_boards_page.go_to_main_page()
    main_page = MainPage(browser)
    main_page.create_private_board(board_name)
    all_boards_page.open()
    return all_boards_page
