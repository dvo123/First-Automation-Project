from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage
from pages.vacancy_page import VacancyPage

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
            vacancy_name="Automation Tester For 11/06",
            description="Automation Test is Running",
            hiring_manager="AtAZcsQrmUCHINU ffhvvXcJSUDHA WepKDUmDRqSELVA KUMAR",
            number_of_positions="1"
        )
        