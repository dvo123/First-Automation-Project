from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage

class TestRecruitment:

    def test_recruitment(self, driver):
        login_page = LoginPage(driver)
        recruitment_page = RecruitmentPage(driver)

        login_page.login("Admin", "admin123")
        recruitment_page.click_recruitment()
        recruitment_page.click_search()
        recruitment_page.click_vancancies()