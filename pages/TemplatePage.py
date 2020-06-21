import allure
from pages.BasePage import BasePage
from pages.locators import TemplatePageLocators
import time


class TemplatePage(BasePage, TemplatePageLocators):
    path = ''

    @allure.step("Create new board {name} from template")
    def create_board_from_tmpl(self, name):
        self._wait_for_visibility(self.USE_TMPL_BTN)
        time.sleep(3)
        self._click(self.USE_TMPL_BTN)
        self._input(self.BOARD_NEW_TITLE_INPUT, name)
        self._click(self.CREATE_BOARD_FROM_TMPL_BTN)
