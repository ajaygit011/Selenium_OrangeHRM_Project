import pytest
from selenium import webdriver
from configs.AutoConfigConstants import AutoConstants


@pytest.fixture(scope='class')
def init_driver(request):
    web_driver = webdriver.Chrome(executable_path=AutoConstants.EXECUTABLE_PATH)
    request.cls.driver = web_driver
    web_driver.maximize_window()
    web_driver.implicitly_wait(10)
    web_driver.delete_all_cookies()
    web_driver.get(AutoConstants.url)
    yield
    web_driver.quit()
