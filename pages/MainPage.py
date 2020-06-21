import allure
import time
from .BasePage import BasePage
from pages.locators import MainPageLocators, CreateBoardWindowLocators


class MainPage(BasePage, MainPageLocators, CreateBoardWindowLocators):
    path = '/'

    @allure.step("Go to templates")
    def go_to_templates(self):
        self._click(self.TEMPLATES_BTN)
