from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from src.enums.global_enums import GlobalErrorMessages
from src.enums.main_page_enums import MainPageEnums


class MainPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = MainPageEnums.URL.value
        self.__search_input_xpath = "//*[@data-qa='search-input']"
        self.__search_button_xpath = "//*[@data-qa='search-button']"
        self.__advancedSearch_xpath = "//*[@data-qa='advanced-search']"
        self.__promo_header_xpath = "//*[@data-qa='bloko-header-3']"
        self.__mainmenu_employer_xpath = "//*[@data-qa='mainmenu_employer']"

    def get_search_input(self) -> WebElement:
        return self.is_visible('xpath', self.__search_input_xpath, 'Main search input')

    def get_search_button(self) -> WebElement:
        return self.is_visible('xpath', self.__search_button_xpath, 'Main search button')

    def get_promo_header(self) -> WebElement:
        return self.is_visible('xpath', self.__promo_header_xpath, 'Promo header')

    def get_advanced_search_button(self) -> WebElement:
        return self.is_visible('xpath', self.__advancedSearch_xpath, 'Advanced search btn')

    def get_mainmenu_employer(self) -> WebElement:
        return self.is_visible('xpath', self.__mainmenu_employer_xpath, 'Main menu employer btn')

    def enter_text_in_search_input(self, text):
        search_input = self.get_search_input()
        search_input.click()
        search_input.send_keys(text)

    def click_search_button(self):
        search_button = self.get_search_button()
        search_button.click()

    def assert_promo_text(self):
        promo_header = self.get_promo_header()
        assert promo_header.text == MainPageEnums.PROMO_HEADER_TEXT.value, GlobalErrorMessages.WRONG_TEXT.value

    def click_advanced_search_button(self):
        advanced_search_button = self.get_advanced_search_button()
        advanced_search_button.click()

    def click_mainmenu_employer(self):
        mainmenu_employer = self.get_mainmenu_employer()
        mainmenu_employer.click()

    def assert_page_url(self):
        current_url = self.driver.current_url
        assert current_url == self.url




