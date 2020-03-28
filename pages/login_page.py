from .base_page import BasePage
from .locators import LoginPageLocarors

from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'This is not the login page.'

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocarors.LOGIN), 'There is no login form'

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocarors.REGISTER), 'There is no sign out form'