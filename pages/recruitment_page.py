import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage

class RecruitmentPage:
    
    def __init__(self, driver):
        self.driver = driver

        self.recruitment_btn = (By.XPATH,'//a[@href="/web/index.php/recruitment/viewRecruitmentModule"]')
        self.search_btn = (By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]')

        self.vancancies_btn = (By.XPATH,"//a[text()='Vacancies']")

    def click_recruitment(self):
        self.driver.find_element(*self.recruitment_btn).click()
        return WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.recruitment_btn))
    def click_search(self):
        self.driver.find_element(*self.search_btn).click()
        return WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.search_btn))
    def click_vancancies(self):
        self.driver.find_element(*self.vancancies_btn).click()
        return WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.vancancies_btn))