from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_has_not_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket contains an item, but should not"

    def get_message_about_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Basket is not empty"