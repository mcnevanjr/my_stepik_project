from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner .product_main h1")
    ADDED_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages .alert.alert-safe.alert-noicon.alert-success.fade.in")
    PRODUCT_NAME_ADDED_IN_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner .price_color")
    TOTAL_PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner")
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner strong")
