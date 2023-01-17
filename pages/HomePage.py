from base.BasePage import BasePage


class HomePage(BasePage):
    pim_page = "//span[text()='PIM']"
    add_emp_button = "//a[text()='Add Employee']"
    emp_list_button = "//a[text()='Employee List']"
    first_name_field = "//input[@name='firstName']"
    middle_name_field = "//input[@name='middleName']"
    last_name_field = "//input[@name='lastName']"
    emp_id_field = "//label[text()='Employee Id']/../parent::div//input"
    save_emp_button = "//button[text()=' Save ']"
    success_msg = "//div[@class='oxd-toast-content oxd-toast-content--success']//p[contains(@class,'toast-message')]"

    '''Employee List Page Locators'''
    employee_name = ""
    emp_id_search = "//label[text()='Employee Id']/../parent::div//input"
    search_btn = "//button[text()=' Search ']"
    record_found_txt = "//span[contains(text(),'Record Found')]"
    edit_emp_title = "//h6[text()='Personal Details']"
    emp_details = "//div[@class='oxd-table-card']//div[contains(@class,'oxd-table-cell')]//div[text()]"

    '''Edit Employee Page Locators'''
    delete_pop_up_message = "//div[contains(@class,'oxd-sheet')]//div[@class='orangehrm-text-center-align']"
    delete_confm_button = "//button[text()=' Yes, Delete ']"

    def __init__(self, driver):
        super().__init__(driver)

    # click on PIM button on home page
    def navigate_To_Pim_Page(self):
        self.safe_click(self.pim_page)

    # click on add employee option
    def click_add_employee_option(self):
        self.safe_click(self.add_emp_button)

    # clear the employee id field
    def clear_emp_id_field(self):
        self.clear(self.emp_id_field)

    # open add employee , enter employee details
    def add_employee(self, firstname, middlename, lastname, employee_id):
        self.enter_text(self.first_name_field, firstname)
        self.enter_text(self.middle_name_field, middlename)
        self.enter_text(self.last_name_field, lastname)
        self.enter_text(self.emp_id_field, employee_id)

    # open employee list section
    def click_employee_list(self, locator):
        self.click(self.emp_list_button)

    # click on save button of the employee details
    def save_employee_details(self):
        self.wait_for_element_clickable(self.save_emp_button)
        self.scroll_into_view(self.save_emp_button)
        self.click_element_using_js(self.save_emp_button)
        self.log_info('click on save button')

    '''get delete/save success msg at the bottom of the page / on pop-up'''
    def get_success_msg(self):
        self.wait_for_element(self.success_msg)
        return self.get_element_text(self.success_msg)

    '''navigate to emp list section'''

    def navigate_to_empList(self):
        self.safe_click(self.emp_list_button)
        self.log_info("navigated to employee list page")

    '''search employee by emp_id'''

    def search_employee_by_id(self, emp_id_value):
        self.clear(self.emp_id_search)
        self.enter_text(self.emp_id_search, emp_id_value)
        self.safe_click(self.search_btn)

    def verify_search_emp_presence(self, emp_id_value):
        emp_id_value = str(emp_id_value)
        emp_id_result = "//div[@class='oxd-table-body']//div[text()='" + emp_id_value + "']"
        self.scroll_into_view(self.search_btn)
        return self.is_element_visible(emp_id_result)

    '''click  on pen icon to edit the employee details'''

    def edit_emp_details(self, emp_id):
        str_emp_id = str(emp_id)
        ele = "//div[@class='oxd-table-body']//div[text()='" + str_emp_id + "']/../parent::div//i[contains(@class,'bi-pencil')]"
        self.safe_click(ele)

    '''returns true if edit employee details form is open'''

    def verify_edit_page_is_open(self):
        return self.is_element_visible(self.edit_emp_title)

    '''update firstname of the employee'''

    def update_emp_fname(self, value):
        self.clear(self.first_name_field)
        self.enter_text(self.first_name_field, value);

    '''click on bin icon of the employee '''

    def delete_employee(self, emp_id):
        str_emp_id = str(emp_id)
        delete_button = "//div[text()='" + str_emp_id + "']/../..//div//i[contains(@class,'bi-trash')]"
        self.safe_click(delete_button)
        self.log_info("Clicked  on delete button")

    '''get the text of delete pop-up button'''

    def verify_delete_pop_up_message(self):
        self.wait_for_element(self.delete_pop_up_message)
        return self.get_element_text(self.delete_pop_up_message)

    '''click on Yes, delete button on the pop-up to delete the record permanently'''

    def delete_record_permanently(self):
        self.safe_click(self.delete_confm_button)

    def get_employee_details(self):
        self.scroll_into_view(self.emp_details)
        list_01= self.get_elements_text(self.emp_details)
        return list_01