import allure
from pages.BasePage import BasePage
from pages.locators import AllBoardsPageLocators, CreateBoardWindowLocators
from selenium.common.exceptions import NoSuchElementException


class AllBoardsPage(BasePage, AllBoardsPageLocators, CreateBoardWindowLocators):
    path = '/ellensshi/boards'

    def __find_board_by_name(self, board_name):
        boards = self._elements(self.PERSONAL_BOARDS_NAMES)
        for board in boards:
            board_title = self._get_element_attribute(board, "title")
            if board_title == board_name:
                return board
        return None

    @allure.step("Create private board")
    def create_private_board(self, board_name):
        self._click(self.CREATE_NEW_BOARD_BTN)
        self._input(self.BOARD_NAME_INPUT, board_name)
        self._click(self.CREATE_SUBMIT_BTN)

    @allure.step("Open board {board_name}")
    def go_to_board(self, board_name):
        board = self.__find_board_by_name(board_name)
        if board:
            board.click()
        else:
            raise NoSuchElementException(f"Board with name {board_name} is absent")

    @allure.step("Go to main page")
    def go_to_main_page(self):
        self._click(self.MAIN_PAGE_BTN)

    @allure.step("Go to templates")
    def go_to_templates(self):
        self._click(self.TEMPLATES_BTN)

    @allure.step("Verify if board is present")
    def verify_board_presence(self, board_name):
        board = self.__find_board_by_name(board_name)
        if board:
            return True
        else:
            return False
