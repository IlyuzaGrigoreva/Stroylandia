from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".listing_v24-product-card__basket-button__text")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".fb-product-card__price-value")

    def add_product_to_cart(self):
        self.click(*self.ADD_TO_CART_BUTTON)

    def get_product_price(self):
        price_text = self.get_text(*self.PRODUCT_PRICE).replace('₽/шт', '').replace(' ', '')  # Удаляем символ ₽ и пробелы
        return float(price_text)