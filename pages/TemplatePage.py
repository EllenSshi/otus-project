from pages.BasePage import BasePage
from pages.locators import TemplatePageLocators
import time


class TemplatePage(BasePage, TemplatePageLocators):
    path = ''

    def create_board_from_tmpl(self, name):
        self._wait_for_visibility(self.USE_TMPL_BTN, 1)
        time.sleep(5)
        self._click(self.USE_TMPL_BTN, 1)
        self._input(self.BOARD_NEW_TITLE_INPUT, name)
        self._click(self.CREATE_BOARD_FROM_TMPL_BTN)
