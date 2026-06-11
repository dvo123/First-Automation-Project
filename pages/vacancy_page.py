import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage

class VacancyPage:
    
    def __init__(self, driver):
        self.driver = driver

        self.add_btn = (By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]')
        self.find_title = (By.XPATH,"//h6[text()='Add Vacancy']")

        self.vacancy_name_field = (By.NAME, "username")
        self.jobtitle_dropdown_btn = (By.XPATH, '//i[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"]')
        self.selectAutomationTester_field = (By.XPATH,"//span[text()='Automaton Tester']")
        self.description_field = (By.NAME, "description")
        self.hiringManager_field = (By.NAME, "hiring manager")
        self.numberOfPositions_field = (By.NAME, "number of positions")
        self.active_switch = (By.CSS_SELECTOR, "span.oxd-switch-input")
        self.publish_switch = (By.XPATH,"//span[contains(@class,'oxd-switch-input')]")

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
        hiring_manager,
        number_of_positions
):
        # Vacancy Name
        self.driver.find_element(*self.vacancy_name_field).send_keys(vacancy_name)

        # Job Title dropdown
        self.driver.find_element(*self.jobtitle_dropdown_btn).click()

        WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.selectAutomationTester_field)).click()

        # Description
        self.driver.find_element(*self.description_field).send_keys(description)

        # Hiring Manager
        self.driver.find_element(*self.hiringManager_field).send_keys(hiring_manager)

        # Number of Positions
        self.driver.find_element(*self.numberOfPositions_field).send_keys(number_of_positions)

        # Set Active = False
        self.set_switch_false()

        # Set Active = Active
        self.is_switch_active()
        
    def set_switch_false(self):
        switch = self.driver.find_element(*self.active_switch)

        if "oxd-switch-input--active" in switch.get_attribute("class"):
            switch.click()

    def is_switch_active(self):
        switch = self.driver.find_element(*self.publish_switch)
        return "oxd-switch-input--active" in switch.get_attribute("class")