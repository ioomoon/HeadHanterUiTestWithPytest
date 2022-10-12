from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from src.enums.employer_main_page_enums import EmployerMainPageEnums


class EmployerMainPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = EmployerMainPageEnums.URL.value
        self.__employer_index_title_xpath = "//*[@data-qa='employer-index-title']"
        self.__mainmenu_applicant_xpath = "//*[@data-qa='mainmenu_applicant']"

    def get_employer_index_title(self) -> WebElement:
        return self.is_visible('xpath', self.__employer_index_title_xpath, 'Employer page title')

    def get_mainmenu_applicant(self) -> WebElement:
        return self.is_visible('xpath', self.__mainmenu_applicant_xpath, 'Main menu applicant btn')

    def assert_title_text(self):
        assert self.get_employer_index_title().text == EmployerMainPageEnums.PROMO_HEADER_TEXT.value

    def assert_page_url(self):
        current_url = self.driver.current_url
        assert current_url == self.url

    def click_mainmenu_applicant(self):
        mainmenu_applicant = self.get_mainmenu_applicant()
        mainmenu_applicant.click()
