from selenium.common.exceptions import NoSuchElementException

from pages.BasePage import BasePage
from pages.locators import AllBoardsPageLocators, CreateBoardWindowLocators


class AllBoardsPage(BasePage, AllBoardsPageLocators, CreateBoardWindowLocators):
    path = '/ellensshi/boards'

    def go_to_templates(self):
        self._click(self.TEMPLATES_BTN)

    def go_to_board(self, board_name):
        board = self.__find_board_by_name(board_name)
        if board:
            board.click()
        else:
            raise NoSuchElementException(f"Board with name {board_name} is absent")

    def create_private_board(self, board_name):
        self._click(self.CREATE_NEW_BOARD_BTN)
        self._input(self.BOARD_NAME_INPUT, board_name)
        self._click(self.CREATE_SUBMIT_BTN)

    def verify_board_presence(self, board_name):
        board = self.__find_board_by_name(board_name)
        if board:
            return True
        else:
            return False

    def __find_board_by_name(self, board_name):
        boards = self._elements(self.PERSONAL_BOARDS_NAMES)
        for board in boards:
            board_title = self._get_element_attribute(board, "title")
            if board_title == board_name:
                return board
        return None
