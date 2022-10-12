from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from src.enums.advanced_search_page_enums import AdvancedSearchPageEnums


class AdvancedSearchPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = AdvancedSearchPageEnums.URL.value
        self.__vacancy_search_keywords_input_xpath = "//*[@data-qa='vacancysearch__keywords-input']"
        self.__advanced_search_submit_button_xpath = "//*[@data-qa='advanced-search-submit-button']"
        self.__search_only_in_company_name_text = "//*[contains(text(), 'в названии компании')]"

    def __get_vacancy_search_keywords_input(self) -> WebElement:
        return self.is_visible('xpath', self.__vacancy_search_keywords_input_xpath)

    def enter_text_in_vacancy_search_keywords_input(self, keywords):
        search_input = self.__get_vacancy_search_keywords_input()
        search_input.send_keys(keywords)

    def choose_search_only_in_company_name(self):
        self.is_visible('xpath', self.__search_only_in_company_name_text).click()

    def click_submit_button(self):
        self.is_visible('xpath', self.__advanced_search_submit_button_xpath).click()

    def assert_page_url(self):
        current_url = self.driver.current_url
        assert current_url == self.url
