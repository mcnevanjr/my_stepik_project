from .base_page import BasePage
from .locators import BasketPageLocators

#4.3.10 Задание: наследование и отрицательные проверки
class BasketPage(BasePage):
    def empty_basket_tests(self):
        self.basket_should_be_empty()
        self.basket_is_empty_message()

    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), "Basket might have products added"

    def basket_is_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), "Basket might not be empty"