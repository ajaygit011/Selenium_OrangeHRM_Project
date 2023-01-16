import time

from base.BaseTest import BaseTest
from configs.AutoConfigConstants import AutoConstants
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


class Test_edit_employee(BaseTest):

    def test_edit_employee_01(self):
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.emp_id = AutoConstants.emp_id
        self.login_page.do_user_login(AutoConstants.username, AutoConstants.password)
        self.home_page.navigate_To_Pim_Page()
        self.home_page.click_add_employee_option()

        # clear employee field
        self.home_page.clear_emp_id_field()

        #enter details of an employee
        self.home_page.add_employee("amai", "bssb", "kkns", self.emp_id)

        #save the employee details
        self.home_page.save_employee_details()

        #navigate to employee list page
        self.home_page.navigate_to_empList()

        #search employee by id
        self.home_page.search_employee_by_id(self.emp_id)

        #verify the employee with added employee id is present in the table
        assert  True == self.home_page.verify_search_emp_presence(self.emp_id)

        #update the employee details
        self.home_page.edit_emp_details(self.emp_id)

        #verify edit employee details page is open
        assert True == self.home_page.verify_edit_page_is_open()

        #update the employee name to jessi
        self.home_page.update_emp_fname("jessi")

        #save the employee details after updating the start name
        self.home_page.save_employee_details()

        #naviagte to employee list page and search the employee with the same employee id and verify the updated name in the empoloyee details
        self.home_page.navigate_to_empList()

        self.home_page.search_employee_by_id(self.emp_id)
        time.sleep(30)










