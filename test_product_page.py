from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_name()
    page.should_be_product_cost()
    page.should_be_add_product_in_busket()
    page.press_add_product_in_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_name_add_to_basket()
    page.should_be_basket_total_cost()
    page.name_product_in_basket_equal_name_product()
    page.price_product_equal_basket_total_cost()
