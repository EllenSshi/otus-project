from selenium.webdriver.common.by import By


class AllBoardsPageLocators:
    PERSONAL_BOARDS_NAMES = (By.CSS_SELECTOR, '.content-all-boards .board-tile-details-name')
    CREATE_NEW_BOARD_BTN = (By.CSS_SELECTOR, '.mod-add')


class AllTemplatesPageLocators:
    PERSONAL_SECTION = (By.CSS_SELECTOR, 'li[data-test-id="templates"] a[href="/templates/personal"]')
    READING_LIST_TMPL = (By.CSS_SELECTOR, 'a[href="/templates/personal/reading-list-sy79W3jy"]')


class BasePageLocators:
    HOME_BTN = (By.CSS_SELECTOR, 'span[name=house]')
    BOARDS_BTN = (By.CSS_SELECTOR, 'button[data-test-id=header-boards-menu-button]')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'data-test-id=header-search-input')
    USER_BTN = (By.CSS_SELECTOR, 'button[data-test-id=header-member-menu-button]')
    LOGOUT_BTN = (By.CSS_SELECTOR, 'button[data-test-id="header-member-menu-logout"]')
    MAIN_LOGIN_BTN = (By.CSS_SELECTOR, 'a[href="/login"]')

    ALL_BOARDS_BTN = (By.CSS_SELECTOR, 'a[href*="/boards"]')
    TEMPLATES_BTN = (By.CSS_SELECTOR, 'li[data-test-id=templates]')
    MAIN_PAGE_BTN = (By.CSS_SELECTOR, 'a[data-test-id=home-link]')
    CREATE_BOARD_BTN = (By.CSS_SELECTOR, 'button._1Gg_uYRwKI5VOY')


class BoardPageLocators:
    BOARD_NAME = (By.CSS_SELECTOR, '.js-board-name-input')
    ABOUT_BOARD_BTN = (By.CSS_SELECTOR, '.js-about-this-board')
    DESCRIPTION_FAKE_AREA = (By.CSS_SELECTOR, 'a.description-fake-text-area')
    DESCRIPTION_AREA = (By.CSS_SELECTOR, 'textarea.board-description')
    SAVE_DESCRIPTION_BTN = (By.CSS_SELECTOR, 'input.confirm')
    BOARD_DESCRIPTION = (By.CSS_SELECTOR, '.js-desc p')
    ADD_LIST_PLACEHOLDER = (By.CSS_SELECTOR, 'span.placeholder')
    LIST_NAME_INPUT = (By.CSS_SELECTOR, 'input.list-name-input')
    ADD_LIST_BTN = (By.CSS_SELECTOR, 'input.mod-list-add-button')
    LIST_HEADERS = (By.CSS_SELECTOR, 'h2.list-header-name-assist')


class CreateBoardWindowLocators:
    BOARD_NAME_INPUT = (By.CSS_SELECTOR, 'input[data-test-id=create-board-title-input]')
    BOARD_TYPE_BTN = (By.CSS_SELECTOR, 'button.subtle-chooser-trigger')
    PRIVATE_TYPE = (By.CSS_SELECTOR, '.vis-chooser .icon-private')
    PUBLIC_TYPE = (By.CSS_SELECTOR, '.vis-chooser .icon-public')
    CREATE_SUBMIT_BTN = (By.CSS_SELECTOR, 'button[data-test-id=create-board-submit-button]')


class LoginPageLocators:
    USER_INPUT = (By.CSS_SELECTOR, '#user')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#password')
    LOGIN_ATLASSIAN_BTN = (By.CSS_SELECTOR, '#login[value="Log in with Atlassian"]')
    LOGIN_ATLASSIAN_BTN2 = (By.CSS_SELECTOR, '#login[value="Войти с помощью Atlassian"]')
    LOGIN_BTN = (By.CSS_SELECTOR, '#login-submit')
    LOGIN_ERROR_MSG = (By.CSS_SELECTOR, 'div#login-error')


class MainPageLocators:
    pass


class TemplatePageLocators:
    USE_TMPL_BTN = (By.CSS_SELECTOR, "div>button[type=button]:nth-child(2)")
    BOARD_NEW_TITLE_INPUT = (By.CSS_SELECTOR, '#boardNewTitle')
    CREATE_BOARD_FROM_TMPL_BTN = (By.CSS_SELECTOR, 'form > input[type=submit]')
