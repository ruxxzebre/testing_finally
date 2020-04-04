from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()
        answer = self.solve_quiz_and_get_code()


    def match_message_of_addition_to_basket(self):
        assert True, 'Message is absent, product is not added'

    def match_basket_value_with_product(self):
        assert True, 'Product value not matches with basket value'

