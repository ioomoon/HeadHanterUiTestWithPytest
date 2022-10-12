from selenium.common import TimeoutException
from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class ResultPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__vacancies_total_found_xpath = "//*[@data-qa='vacancies-total-found']"
        self.__vacancy_not_found_xpath = "//*[contains(text(), 'ничего не найдено')]"
        self.__vacancy_serp_vacancy_class = "serp-item"

    def get_vacancies_total_found(self) -> WebElement:
        return self.is_visible('xpath', self.__vacancies_total_found_xpath, 'Vacancies total')

    def get_vacancy_serp_list(self) -> List[WebElement]:
        return self.are_visible('class_name', self.__vacancy_serp_vacancy_class, 'Result of vacancy search')

    def assert_vacancy_results_exist(self):
        vacancy_results = self.get_vacancy_serp_list()
        assert len(vacancy_results) > 0

    def assert_vacancy_results_not_exist(self):
        try:
            vacancy_result = self.are_visible('xpath', self.__vacancy_serp_vacancy_class, 'Results of vacancy search')
        except TimeoutException:
            vacancy_result = None
        assert vacancy_result is None

    def assert_text_about_results_not_exist(self, vacancy_name):
        text_about_results_not_exist = self.is_visible('xpath', self.__vacancy_not_found_xpath).text
        assert text_about_results_not_exist == "По запросу «" + vacancy_name + "» ничего не найдено"



