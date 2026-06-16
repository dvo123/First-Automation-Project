from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage
from pages.vacancy_page import VacancyPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestVacancy:

    def test_recruitment(self, driver):
        login_page = LoginPage(driver)
        recruitment_page = RecruitmentPage(driver)
        vacancy_page = VacancyPage(driver)

        print("Login")
        login_page.login("Admin", "admin123")

        print("Recruitment")
        recruitment_page.click_recruitment()

        print("Vacancies")
        recruitment_page.click_vancancies()

        print("Add")
        vacancy_page.click_add()

        print("Verify")
        assert vacancy_page.get_page_title() == "Add Vacancy"

        print("Add Vacancy")
        vacancy_page.add_vacancy(
            vacancy_name="Automation Tester For 11/07",
            description="Automation Test is Running",
            number_of_positions="01"
        )

        print("Recruitment")
        WebDriverWait(self.driver, 6).until(
            EC.visibility_of_element_located(recruitment_page.click_recruitment())
        )
        # Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
        # Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression

        # scoop install allure
        # pip install allure-pytest

