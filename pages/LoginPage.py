from base.BasePage import BasePage


class LoginPage(BasePage):
    logo = "//img[@alt='company-branding']"
    user_name_field = "//input[@name='username']"
    password_field = "//input[@name='password']"
    login_button = "//button[@type='submit']"

    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
        return self.driver.title

    def is_logo_visible(self):
        self.wait_for_element(self.logo)
        return self.is_element_visible(self.logo)

    def do_user_login(self, username, password):
        self.enter_text(self.user_name_field, username)
        self.enter_text(self.password_field, password)
        self.safe_click(self.login_button)
