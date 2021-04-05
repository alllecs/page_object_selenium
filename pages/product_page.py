from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_product_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BUSKET), "Add to basket button isn't presented"

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name isn't presented"

    def should_be_product_cost(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_COST), "Product cost isn't presented"

    def press_add_product_in_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BUSKET)
        login_link.click()

    def should_be_product_name_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRODUCT_NAMES), \
            "The name of the product added to the cart is not specified"

    def should_be_basket_total_cost(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL), "Basket total cost isn't presented"

    def name_product_in_basket_equal_name_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_to_basket = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAMES)
        assert product_name.text == product_name_to_basket.text, "Name in basket and product name isn't equal"

    def price_product_equal_basket_total_cost(self):
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST)
        basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        assert product_cost.text == basket_cost.text, "Prices in basket and in product page isn't equal"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message isn't presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should be disappeared"
