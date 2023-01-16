import logging

from base.BasePage import BasePage
from base.BaseTest import BaseTest
from configs.AutoConfigConstants import AutoConstants
from pages.LoginPage import LoginPage


class Test_login(BaseTest):

    def test_login_title(self):
        self.login_page = LoginPage(self.driver)
        title = self.login_page.get_title()
        assert title == AutoConstants.title, "Title of the application did not match"


    def test_login_logo_visible(self):
        self.login_page = LoginPage(self.driver)
        assert True == self.login_page.is_logo_visible()

    def test_do_login(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_user_login(AutoConstants.username,AutoConstants.password)