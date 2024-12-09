from selenium.webdriver.common.by import By
from .base_page import BasePage
import time
from selenium import webdriver

class CartPage(BasePage):
    TOTAL_PRICE = (By.XPATH, "//div[contains(text(), 'Итого')]/following-sibling::div[@class='total-row__value']")
    CART_QUANTITY_BUTTON = (By.CSS_SELECTOR, '.counter__plus')

    def increase_quantity(self):
        self.click(*self.CART_QUANTITY_BUTTON)

    def get_total_price(self):
        time.sleep(2)
        price_text = self.get_text(*self.TOTAL_PRICE).replace('₽', '').replace(' ', '')
        return float(price_text)

