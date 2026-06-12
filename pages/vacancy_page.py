import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class VacancyPage:
    
    def __init__(self, driver):
        self.driver = driver

        self.add_btn = (By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]')
        self.find_title = (By.XPATH,"//h6[text()='Add Vacancy']")

        self.vacancy_name_field = (By.NAME, "username")
        self.vacancy_name_field = (By.XPATH,"//label[normalize-space()='Vacancy Name']/ancestor::div[contains(@class,'oxd-input-group')]//input")
        self.job_title_dropdown_btn = (By.XPATH, '//i[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"]')
        self.selectAutomationTester_field = (By.XPATH,"//span[text()='Automaton Tester']")
        self.description_field = (By.XPATH,"//textarea[@placeholder='Type description here']")
        self.hiringManager_field = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.numberOfPositions_field = (By.XPATH,"//label[normalize-space()='Number of Positions']/ancestor::div[contains(@class,'oxd-input-group')]//input")
        self.active_switch = (By.XPATH,"//p[normalize-space()='Active']/following::span[contains(@class,'oxd-switch-input')][1]")
        self.publish_switch = (
            By.XPATH,
            "//p[normalize-space()='Publish in RSS Feed and Web Page']/following-sibling::div//span[contains(@class,'oxd-switch-input')]"
        )
        self.save_btn = (By.XPATH,"//button[normalize-space()='Save']")


    def click_add(self):
        self.driver.find_element(*self.add_btn).click()

        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(*self.find_title)
        )

    def get_page_title(self):
        return WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(*self.find_title)
        ).text
    
    def add_vacancy(
        self,
        vacancy_name,
        description,
        number_of_positions
):
        # Vacancy Name
        print("Entering Vacancy Name")
        self.driver.find_element(*self.vacancy_name_field).send_keys(vacancy_name)

        # Job Title dropdown
        print("Clicking Job Title dropdown")
        dropdown = WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.job_title_dropdown_btn))
        dropdown.click()

        print("Selecting Job Title")
        WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.selectAutomationTester_field)).click()

        # Description
        print("Entering Description")
        self.driver.find_element(*self.description_field).send_keys(description)

        # Hiring Manager
        print("Entering Hiring Manager")
        recruitment_page = RecruitmentPage(self.driver)

        manager_name = recruitment_page.get_name()

        field = self.driver.find_element(*self.hiringManager_field)

        field.send_keys(manager_name)

        # Wait for "Searching..." to disappear and real result to appear
        option = WebDriverWait(self.driver, 15).until(
            lambda d: d.find_element(
                By.XPATH,
                "//div[@role='option'][not(contains(.,'Searching'))]"
            )
        )

        print("Found manager:", option.text)

        option.click()

        # Number of Positions
        print("Entering Number of Positions")
        self.driver.find_element(*self.numberOfPositions_field).send_keys(number_of_positions)

        # Set Active = False
        print("Setting Active to False")
        self.set_active_false()
        assert self.is_active() is False

        # # Set Active = Active
        print("Setting Active to True")
        self.set_publish_true()
        assert self.is_publish_active() is True

        # Save
        print("Saving Vacancy")
        self.driver.find_element(*self.save_btn).click()

    def set_active_false(self):
        switch = self.driver.find_element(*self.active_switch)

        if "oxd-switch-input--active" in switch.get_attribute("class"):
            switch.click()

    def is_active(self):
        switch = self.driver.find_element(*self.active_switch)

        return "oxd-switch-input--active" in switch.get_attribute("class")
    
    def set_publish_true(self):
        switch = self.driver.find_element(*self.publish_switch)

        if "oxd-switch-input--active" not in switch.get_attribute("class"):
            switch.click()

    def is_publish_active(self):
        switch = self.driver.find_element(*self.publish_switch)

        return "oxd-switch-input--active" in switch.get_attribute("class")
    
# setTimeout(() => {
#     debugger;
# }, 5000);