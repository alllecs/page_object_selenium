import pytest
from faker import Faker
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

@pytest.mark.register
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        f = Faker()
        email = f.email()
        password = f.password()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_name()
        page.should_be_product_cost()
        page.should_not_be_success_message()
        page.should_be_add_product_in_basket()
        page.press_add_product_in_basket()
        page.solve_quiz_and_get_code()
        page.should_be_product_name_add_to_basket()
        page.should_be_basket_total_cost()
        page.name_product_in_basket_equal_name_product()
        page.price_product_equal_basket_total_cost()
        page.should_be_success_message()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                               marks=pytest.mark.xfail(reason="some bug")),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(self, browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_name()
    page.should_be_product_cost()
    page.should_not_be_success_message()
    page.should_be_add_product_in_basket()
    page.press_add_product_in_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_name_add_to_basket()
    page.should_be_basket_total_cost()
    page.name_product_in_basket_equal_name_product()
    page.price_product_equal_basket_total_cost()
    page.should_be_success_message()

def test_guest_cant_see_success_message(self, browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="message is on page after add to basket")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_in_basket()
    page.press_add_product_in_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="message is in not disappeared after add to basket")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_in_basket()
    page.press_add_product_in_basket()
    page.solve_quiz_and_get_code()
    page.should_be_disappeared_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    page.basket_has_not_products()
    page.get_message_about_basket_is_empty()
