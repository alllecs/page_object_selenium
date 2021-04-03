from .base_page import BasePage
from .locators import LoginPageLocators
#from selenium.common.exceptions import NoSuchElementException

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        name_in_link = "accounts/login/"
        print(self.browser.current_url)
        assert name_in_link in self.browser.current_url, print(self.browser.current_url)
        #assert self.current_url(BasePage.url) == login_link, "Url is not corrected"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_LINK), "Register link is not presented"