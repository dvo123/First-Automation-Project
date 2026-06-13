import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver):
        # khơi tạo driver để giúp tương tác với Chrome
        self.driver = driver
    def find_element(self, locator):
         return WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*locator))
        
    def click (self, locator):
        self.driver.find_element(*locator).click()

    def send_keys(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def is_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()
        
    def select_option_from_dropdown(self, dropdown_locator, option_text):
        dropdown = self.driver.find_element(*dropdown_locator)

        # Try native <select> first
        try:
            select = Select(dropdown_locator)
            # try select by visible text
            return
        except Exception:
            # Not a native select element - fail back to clicking
            return None