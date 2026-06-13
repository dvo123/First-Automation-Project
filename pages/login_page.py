import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.click_btn = (By.XPATH, '//button[@type="submit"]')
        self.upgrade_btn = (By.XPATH, '//button[@class="oxd-glass-button orangehrm-upgrade-button"]')

    def login(self, username, password):
        self.send_keys(self.username_field, username)
        self.send_keys(self.password_field, password)
        self.click(self.click_btn)

    def click_upgrade(self):
        self.is_displayed(self.upgrade_btn)