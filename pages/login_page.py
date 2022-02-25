from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        self.register_new_user()

    def register_new_user(self):
        # который принимает две строки и регистрирует пользователя. Реализуйте его, описав соответствующие элементы страницы.
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "psw1!"
        self.browser.implicitly_wait(10)
        email_address = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        email_address.send_keys(email)
        psw = self.browser.find_element(*LoginPageLocators.REGISTER_PSW_FIELD)
        psw.send_keys(password)
        psw_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PSW_FIELD)
        psw_confirm.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()

    def should_be_login_url(self):
        assert self.browser.current_url.find("login") != -1, "Login link is incorrect"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"