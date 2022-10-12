import pytest
from tests.steps.allure_steps import *


@pytest.mark.usefixtures('setup')
class TestApplicantPart:

    @allure.title("Checking the promotional text on the main page")
    def test_promo_header(self):
        with allure.step("Initializing the main page"):
            main_page = MainPage(self.driver)
            main_page.assert_page_url()
        with allure.step("Checking that the promo text is correct"):
            main_page.assert_promo_text()

    @allure.title("Checking search results by job title")
    @pytest.mark.parametrize('vacancy_name', [
        "qa engineer", "тестировщик", "специалист по тестированию"
    ])
    def test_search(self, vacancy_name):
        initialize_main_page(self, vacancy_name)
        with allure.step("Checking that there is information about the number of received vacancies"):
            result_page = ResultPage(self.driver)
            result_page.get_vacancies_total_found()
        checking_that_vacancy_results_exist(self)

    @allure.title("Checking search results by wrong job title")
    @pytest.mark.parametrize('vacancy_name', [
        "there is nothing here", "there is no such profession"
    ])
    def test_search_with_wrong_vacancy(self, vacancy_name):
        initialize_main_page(self, vacancy_name)
        with allure.step("Check that there are no search results"):
            result_page = ResultPage(self.driver)
            result_page.assert_vacancy_results_not_exist()
            result_page.assert_text_about_results_not_exist(
                vacancy_name)

    @allure.title("Checking advanced search results by company name")
    @pytest.mark.parametrize('company_name', [
        "headhunter", "тинькофф"
    ])
    def test_advanced_search(self, company_name):
        open_advanced_search(self)
        checking_advanced_search_page_url(self)
        advanced_search_by_keywords_in_company_name(self, company_name)
        checking_that_vacancy_results_exist(self)

    @allure.title("Go to the page for employers")
    def test_change_status_to_employer(self):
        open_main_employer_page_from_main(self)
        checking_main_employer_page_url(self)
        checking_main_employer_page_title(self)

    @allure.title("Go to the page for applicants")
    def test_change_status_to_applicant(
            self):
        open_main_employer_page_from_main(self)
        open_main_applicant_page_from_employer(self)
        checking_main__page_url(self)
