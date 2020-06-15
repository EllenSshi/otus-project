from .BasePage import BasePage
from pages.locators import MainPageLocators, CreateBoardWindowLocators


class MainPage(BasePage, MainPageLocators):
    path = '/'

    def create_private_board(self):
        pass

    def create_public_board(self):
        pass
