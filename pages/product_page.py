from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_added_to_basket(self):
        self.add_product_to_basket()   #добавить продукт в корзину
        self.product_was_added_message()  #сообщение о том, что товар добавлен в корзину
        self.added_product_name_is_correct() #наименование товара в корзине корректное
        self.basket_total_price_message()   #сообщение со стоимостью корзины
        self.added_product_price_is_correct() #стоимость товара корректная в сообщении со стоимостью корзины

    def add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        link.click()

    def added_product_price_is_correct(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE)
        assert product_price.text == product_price_in_message.text, "Product price in the message isn't correct"

    def added_product_name_is_correct(self):
        product_added_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADDED_IN_MESSAGE)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert product_added_name.text == product_name.text, "Product name in the basket isn't correct"

    def basket_total_price_message(self):
        assert self.is_element_present(*ProductPageLocators.TOTAL_PRICE_MESSAGE), "There is no message containing the total price of the products added"

    def product_was_added_message(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE), "There is no message that the product was added to the basket"

    def should_not_be_success_message(self): #проверка отсутствия сообщения об успешном добавлении товара, когда корзина пустая
        assert self.is_not_element_present(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE), "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE), "Success message didn't dissapear"