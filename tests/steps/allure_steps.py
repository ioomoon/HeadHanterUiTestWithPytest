import allure

from pages.main_page import MainPage
from pages.employer_main_page import EmployerMainPage
from pages.advanced_search_page import AdvancedSearchPage
from pages.result_page import ResultPage


@allure.step("Search on the main page by the 'vacancy_name'")
def initialize_main_page(self, vacancy_name):
    main_page = MainPage(self.driver)
    main_page.enter_text_in_search_input(vacancy_name)
    main_page.click_search_button()


@allure.step("Open the advanced search page")
def open_advanced_search(self):
    main_page = MainPage(self.driver)
    main_page.click_advanced_search_button()


@allure.step("Open the main page for employers")
def open_main_employer_page_from_main(self):
    main_page = MainPage(self.driver)
    main_page.click_mainmenu_employer()


@allure.step("Open the main page from employers page")
def open_main_applicant_page_from_employer(self):
    employer_main_page = EmployerMainPage(self.driver)
    employer_main_page.click_mainmenu_applicant()


@allure.step("Advanced search by keywords 'company_name' in company name")
def advanced_search_by_keywords_in_company_name(self, company_name):
    advanced_search_page = AdvancedSearchPage(self.driver)
    advanced_search_page.assert_page_url()  # Проверяем что открыт корректный урл
    advanced_search_page.enter_text_in_vacancy_search_keywords_input(company_name)
    advanced_search_page.choose_search_only_in_company_name()
    advanced_search_page.click_submit_button()


@allure.step("Checking that the correct URL of advanced search page is open")
def checking_advanced_search_page_url(self):
    advanced_search_page = AdvancedSearchPage(self.driver)
    advanced_search_page.assert_page_url()


@allure.step("Checking that the correct URL of employer main page is open")
def checking_main_employer_page_url(self):
    employer_main_page = EmployerMainPage(self.driver)
    employer_main_page.assert_page_url()  # Проверяем корректность урла


@allure.step("Checking title on employer main page")
def checking_main_employer_page_title(self):
    employer_main_page = EmployerMainPage(self.driver)
    employer_main_page.assert_title_text()  # Проверяем заголовок


@allure.step("Checking that the correct URL of main page is open")
def checking_main__page_url(self):
    main_page = MainPage(self.driver)
    main_page.assert_page_url()  # Проверяем что попали на страницу для соискателей

@allure.step("Checking that the correct URL of main page is open")
def checking_that_vacancy_results_exist(self):
    result_page = ResultPage(self.driver)
    result_page.assert_vacancy_results_exist()

