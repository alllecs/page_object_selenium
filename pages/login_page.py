from .base_page import BasePage
from .locators import LoginPageLocators
from time import sleep

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        reg_email.send_keys(email)
        reg_pass1 = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        reg_pass1.send_keys(password)
        reg_pass2 = self.browser.find_element(*LoginPageLocators.REG_REPEAT_PAS)
        reg_pass2.send_keys(password)
        sleep(1)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BTN)
        reg_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        name_in_link = "accounts/login/"
        print(self.browser.current_url)
        assert name_in_link in self.browser.current_url, print(self.browser.current_url)

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_LINK), "Register link is not presented"