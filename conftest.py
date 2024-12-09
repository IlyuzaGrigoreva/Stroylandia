from pathlib import Path
from sys import path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from seleniumbase import Driver

path.append(Path(__file__).parent.as_posix())
pytest_plugins = []

@pytest.fixture(scope='module')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = Driver(uc=True, headless=False)
    url = "https://stroylandiya.ru"
    driver.get(url)
    driver.maximize_window()
    driver.uc_gui_click_captcha()
    yield driver
    driver.quit()