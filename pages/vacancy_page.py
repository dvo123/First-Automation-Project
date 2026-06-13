from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from pages.recruitment_page import RecruitmentPage


class VacancyPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.add_btn = (
            By.XPATH,
            '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'
        )

        self.selectAutomationTester_field = (
            By.XPATH,
            "//span[text()='Automaton Tester']"
        )

        self.find_title = (
            By.XPATH,
            "//h6[text()='Add Vacancy']"
        )

        self.vacancy_name_field = (
            By.XPATH,
            "//label[normalize-space()='Vacancy Name']/ancestor::div[contains(@class,'oxd-input-group')]//input"
        )

        self.job_title_dropdown_btn = (
            By.XPATH,
            '//i[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"]'
        )

        self.description_field = (
            By.XPATH,
            "//textarea[@placeholder='Type description here']"
        )

        self.hiringManager_field = (
            By.XPATH,
            "//input[@placeholder='Type for hints...']"
        )

        self.numberOfPositions_field = (
            By.XPATH,
            "//label[normalize-space()='Number of Positions']/ancestor::div[contains(@class,'oxd-input-group')]//input"
        )

        self.active_switch = (
            By.XPATH,
            "//p[normalize-space()='Active']/following::span[contains(@class,'oxd-switch-input')][1]"
        )

        self.publish_switch = (
            By.XPATH,
            "//p[normalize-space()='Publish in RSS Feed and Web Page']/following-sibling::div//span[contains(@class,'oxd-switch-input')]"
        )

        self.save_btn = (
            By.XPATH,
            "//button[normalize-space()='Save']"
        )

        self.edit_vacancy_title = (
            By.XPATH,
            "//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title']"
        )

    def click_add(self):
        self.click(self.add_btn)
        self.find_element(self.find_title)

    def get_page_title(self):
        return self.find_element(self.find_title).text
    
    def get_edit_vacancy_title(self):
        return self.find_element(self.edit_vacancy_title).text

    def select_job_title(self):
        print("Clicking Job Title dropdown")

        dropdown = WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(*self.job_title_dropdown_btn)
        )
        dropdown.click()

        print("Selecting Job Title")

        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(*self.selectAutomationTester_field)
        ).click()

    def is_switch_active(self, locator):
        return (
            "oxd-switch-input--active"
            in self.find_element(locator).get_attribute("class")
        )

    def set_switch(self, locator, desired_state):
        current_state = self.is_switch_active(locator)

        if current_state != desired_state:
            self.click(locator)

    def set_active_false(self):
        self.set_switch(self.active_switch, False)

    def is_active(self):
        return self.is_switch_active(self.active_switch)

    def set_publish_true(self):
        self.set_switch(self.publish_switch, True)

    def is_publish_active(self):
        return self.is_switch_active(self.publish_switch)
    
    def wait_for_edit_vacancy_page(self, title):
        WebDriverWait(self.driver, 15).until(
        EC.visibility_of_element_located(title)
    )

    def add_vacancy(
        self,
        vacancy_name,
        description,
        number_of_positions,
        job_title="Automation Tester"
    ):
        print("Entering Vacancy Name")
        self.send_keys(self.vacancy_name_field, vacancy_name)

        print("Selecting Job Title")
        self.select_job_title()

        print("Entering Description")
        self.send_keys(self.description_field, description)

        print("Entering Hiring Manager")
        recruitment_page = RecruitmentPage(self.driver)

        manager_name = recruitment_page.get_name()

        self.send_keys(self.hiringManager_field, manager_name)

        option = WebDriverWait(self.driver, 15).until(
            lambda d: d.find_element(
                By.XPATH,
                "//div[@role='option'][not(contains(.,'Searching'))]"
            )
        )

        print("Found manager:", option.text)
        option.click()

        print("Entering Number Of Positions")
        self.send_keys(
            self.numberOfPositions_field,
            str(number_of_positions)
        )

        print("Setting Active = False")
        self.set_active_false()
        assert self.is_active() is False

        print("Setting Publish = True")
        self.set_publish_true()
        assert self.is_publish_active() is True

        print("Saving Vacancy")
        self.click(self.save_btn)

        print("Verify Edit Vacancy")
        edit_title = self.find_element(
            self.edit_vacancy_title
        ).text

        assert edit_title == "Edit Vacancy"


