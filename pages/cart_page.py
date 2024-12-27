from selenium.webdriver.common.by import By
from base_page import BasePage

class CartPage(BasePage):
    # Локаторы
    REMOVE_BUTTONS = (By.CSS_SELECTOR, ".remove-btn")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart-item")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, ".empty-cart h2")
    NOTIFICATION = (By.CSS_SELECTOR, ".notification")

    def open(self):
        self.driver.get(f"{self.base_url}/cart.html")
        return self

    def remove_product(self, index=0):
        buttons = self.driver.find_elements(*self.REMOVE_BUTTONS)
        buttons[index].click()

    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def is_cart_empty(self):
        return self.is_element_visible(self.EMPTY_CART_MESSAGE)