import allure
from pages.BasePage import BasePage
from pages.locators import BoardPageLocators
import time


class BoardPage(BasePage, BoardPageLocators):
    path = ''

    def __find_list_by_name(self, list_name):
        lists = self._elements(self.LIST_HEADERS)
        for list in lists:
            list_title = self._get_element_property("innerText", element=list)
            if list_title == list_name:
                return list
        return None

    @allure.step("Add first description to the board")
    def add_first_description(self, description):
        self._click(self.ABOUT_BOARD_BTN)
        self._click(self.DESCRIPTION_FAKE_AREA)
        self._input(self.DESCRIPTION_AREA, description)
        self._click(self.SAVE_DESCRIPTION_BTN)

    @allure.step("Add list")
    def add_list(self, list_name):
        self._input(self.LIST_NAME_INPUT, list_name)
        self._click(self.ADD_LIST_BTN)

    @allure.step("Verify board description")
    def get_board_description(self):
        return self._get_element_property("innerText", selector=self.BOARD_DESCRIPTION)

    @allure.step("Verify board name")
    def get_board_name(self):
        time.sleep(5)
        return self._get_element_text(self.BOARD_NAME)

    @allure.step("Verify if list is present")
    def verify_list_presence(self, list_name):
        list = self.__find_list_by_name(list_name)
        if list:
            return True
        else:
            return False
