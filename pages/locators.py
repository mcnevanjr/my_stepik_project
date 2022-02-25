from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PSW_FIELD = (By.CSS_SELECTOR, "#id_registration-password1.form-control")
    REGISTER_CONFIRM_PSW_FIELD = (By.CSS_SELECTOR, "#id_registration-password2.form-control")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form .btn.btn-lg.btn-primary")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner .product_main h1")
    ADDED_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages .alert.alert-safe.alert-noicon.alert-success.fade.in")
    PRODUCT_NAME_ADDED_IN_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner .price_color")
    TOTAL_PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner")
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group .btn.btn-default")

class BasketPageLocators():
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")