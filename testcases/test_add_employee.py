import time

from base.BaseTest import BaseTest
from configs.AutoConfigConstants import AutoConstants
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


class Test_add_employee_01(BaseTest):
    def test_home_page_01(self):
        self.login_page = LoginPage(self.driver)
        self.home_page  = HomePage(self.driver)

        self.login_page.do_user_login(AutoConstants.username,AutoConstants.password)
        self.home_page.navigate_To_Pim_Page()
        self.home_page.click_add_employee_option()

        #clear employee field
        self.home_page.clear_emp_id_field()
        time.sleep(3)
        self.home_page.add_employee("aa","bb","cc",AutoConstants.emp_id)
        self.home_page.save_employee_details()

        #get save success msg
        exp_save_msg = self.home_page.get_success_msg()

        #verify the expected save message
        assert exp_save_msg == AutoConstants.save_msg ,"save  message mismatch"

        time.sleep(3)


