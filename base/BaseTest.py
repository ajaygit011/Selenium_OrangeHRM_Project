import pytest


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

    # def __init__(self):
    #     self.driver = webdriver.Chrome(executable_path="D:\\chrome_driver_bin\\chromedriver.exe")
    #
    # def launch_browser(self, url):
    #     self.driver.maximize_window()
    #     self.driver.get(url)
    #     self.driver.implicitly_wait(10)
    #     return self.driver
    #
    # def get_driver(self):
    #     return self.driver
