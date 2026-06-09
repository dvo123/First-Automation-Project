from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage

def test_recruitment(driver):
    # setup driver
    login_page = LoginPage(driver)
    recruitment_page = RecruitmentPage(driver)

    # login action
    login_page.login("Admin", "admin123")

    # button actions
    recruitment_page.click_recruitment()
    recruitment_page.click_search()