from pages.BasePage import BasePage
from pages.locators import AllTemplatesPageLocators


class AllTemplatesPage(BasePage, AllTemplatesPageLocators):
    path = '/templates'

    def go_to_reading_list_template(self):
        self._click(self.PERSONAL_SECTION)
        self._move_to_element(self.READING_LIST_TMPL)

    def search_for_template(self, name):
        pass
