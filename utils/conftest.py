import pytest
from selenium import webdriver
from utils.config_reader import ConfigReader
import allure
from allure_commons.types import AttachmentType

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    if ConfigReader.get_headless():
        options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    driver.implicitly_wait(time_to_wait=10)
    driver.get(ConfigReader.get_base_url())

    yield driver

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    # thực hiện test case và lấy kết quả
    outcome = yield
    report = outcome.get_result()

    # nếu test case thất bại,
    if report.when == "call" and report.failed:
        
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Failed Screenshot",
                attachment_type=allure.attachment_type.PNG
            )