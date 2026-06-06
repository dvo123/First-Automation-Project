import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # khơi tạo driver để giúp tương tác với Chrome
    driver = webdriver.Chrome()
    # phóng to trình duyệt Chrome
    driver.maximize_window()
    # thiết lập thời gian chờ ngầm định cho driver
    driver.implicitly_wait(time_to_wait=10)
    # mở SUT (system under test)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    # trả về driver để sử dụng trong các test case
    yield driver
    # đóng trình duyệt sau khi test case hoàn thành
    driver.quit()