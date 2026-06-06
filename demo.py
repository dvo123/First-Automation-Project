import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
def test_directory(driver):

    username_field = (By.NAME, 'username')
    job_title_field = (By.NAME, 'jobtitle')
    directory_btn = (By.XPATH, '//a[@href="/web/index.php/directory/viewDirectory"]]')
    directory_btn = WebDriverWait(driver, 10).until(lambda d: d.find_element(*directory_btn))

    upgrade_btn = (By.XPATH,'//button[@class="oxd-glass-button orangehrm-upgrade-button"]')

    driver.find_element(*job_title_field_field).send_keys('Hr Manager')
    driver.find_element(*password_field).send_keys('admin123')
    
    driver.find_element(*directory_btn).click()


    assert upgrade_btn.is_displayed()

    recruitment_btn = (By.XPATH,'//a[@href="/web/index.php/recruitment/viewRecruitmentModule"]')
    search_btn = (By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]')

    driver.find_element(*recruitment_btn).click()
    driver.find_element(*search_btn).click()