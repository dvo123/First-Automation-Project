import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.click_btn = (By.XPATH, '//button[@type="submit"]')
        self.upgrade_btn = (By.XPATH, '//button[@class="oxd-glass-button orangehrm-upgrade-button"]')

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.click_btn).click()

    def click_upgrade(self):
        self.driver.find_element(*self.upgrade_btn).click()
        return WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.upgrade_btn))