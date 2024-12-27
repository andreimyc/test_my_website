from selenium.webdriver.common.by import By
from base_page import BasePage

class MainPage(BasePage):
    # Локаторы
    LOGO = (By.CSS_SELECTOR, ".logo-container")
    PRODUCTS_LINK = (By.CSS_SELECTOR, "nav a[href='index.html']")
    CART_LINK = (By.CSS_SELECTOR, "nav a[href='cart.html']")
    ABOUT_LINK = (By.CSS_SELECTOR, "footer a[href='about.html']")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, ".product-card button")
    NOTIFICATION = (By.CSS_SELECTOR, ".notification")
    CART_COUNTER = (By.ID, "cartCounter")

    def open(self):
        self.driver.get(f"{self.base_url}/index.html")
        return self

    def click_logo(self):
        self.click_element(self.LOGO)

    def click_products_link(self):
        self.click_element(self.PRODUCTS_LINK)

    def click_cart_link(self):
        self.click_element(self.CART_LINK)

    def click_about_link(self):
        self.click_element(self.ABOUT_LINK)

    def add_product_to_cart(self, index=0):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        buttons[index].click()

    def is_notification_visible(self):
        return self.is_element_visible(self.NOTIFICATION)

    def get_cart_counter_value(self):
        counter = self.find_element(self.CART_COUNTER)
        return counter.text if counter.is_displayed() else "0"