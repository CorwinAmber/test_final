from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        product_link = self.browser.find_element(*ProductPageLocators.PRODUCT_LINK)
        product_link.click()

    def should_be_add(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_LINK), "Product link is not present"
