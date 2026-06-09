import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage

def test_login(driver):
    # setup driver
    login_page = LoginPage(driver)

    # login action
    login_page.login("Admin", "admin123")
    