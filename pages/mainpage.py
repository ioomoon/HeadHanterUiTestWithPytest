from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement


class MainPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__search_input = 'a11y-search-input'

    def get_search_input(self) -> WebElement:
        return self.is_visible('id', self.__search_input, 'Main search input')
