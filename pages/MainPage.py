import allure
from .BasePage import BasePage
from pages.locators import MainPageLocators, CreateBoardWindowLocators


class MainPage(BasePage, MainPageLocators, CreateBoardWindowLocators):
    path = '/'

    @allure.step("Create private board")
    def create_private_board(self, board_name):
        self._click(self.CREATE_BOARD_BTN)
        self._input(self.BOARD_NAME_INPUT, board_name)
        self._click(self.CREATE_SUBMIT_BTN)

