import pytest
from selenium import webdriver
from utils.config_reader import ConfigReader
import allure
from allure_commons.types import AttachmentType

@pytest.fixture
def driver():
    # khơi tạo driver để giúp tương tác với Chrome
    driver = webdriver.Chrome()
    # phóng to trình duyệt Chrome
    driver.maximize_window()
    # thiết lập thời gian chờ ngầm định cho driver
    driver.implicitly_wait(time_to_wait=10)
    # mở SUT (system under test)
    driver.get(ConfigReader.get_base_url())
    # trả về driver để sử dụng trong các test case
    yield driver
    # đóng trình duyệt sau khi test case hoàn thành
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