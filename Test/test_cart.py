import pytest
from selenium import webdriver
from .pages.main_page import MainPage
from .pages.cart_page import CartPage
from conftest import driver


def test_cart_functionality(driver):
    main_page = MainPage(driver)
    cart_page = CartPage(driver)
    main_page.add_product_to_cart()
    product_price = main_page.get_product_price()
    driver.get('https://stroylandiya.ru/cart')
    cart_page.increase_quantity()
    total_price = cart_page.get_total_price()
    assert total_price == product_price * 2, f"Ожидаемая цена продукта = {product_price}, Суммарная цена {total_price}"
