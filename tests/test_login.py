import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
class TestLogin:
    def test_login(self, driver):
        # setup driver
        login_page = LoginPage(driver)

        # login action
        login_page.login(ConfigReader.get_username(),ConfigReader.get_password())
        login_page.click_upgrade()