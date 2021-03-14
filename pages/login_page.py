from .base_page import BasePage
#from selenium.common.exceptions import NoSuchElementException

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        #try:
        #    self.current_url(BasePage.url)
        #except NoSuchElementException:
        #    assert False
        #assert True

    def should_be_login_form(self):
        try:
            self.is_element_present(*LoginPageLocators.LOGIN_LINK)
        except NoSuchElementException:
            assert False, "No login link"
        assert True

    def should_be_register_form(self):
        try:
            self.is_element_present(*LoginPageLocators.REG_LINK)
        except NoSuchElementException:
            assert False, "No register link"
        assert True