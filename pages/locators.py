from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_form")
    REG_LINK = (By.CSS_SELECTOR, "#register_form")

    REG_EMAIL = (By.ID, "id_registration-email")
    REG_PASSWORD = (By.ID, "id_registration-password1")
    REG_REPEAT_PAS = (By.ID, "id_registration-password2")
    REG_BTN = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_TO_BUSKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_COST = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_PRODUCT_NAMES = (By.CSS_SELECTOR, ".alertinner strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
