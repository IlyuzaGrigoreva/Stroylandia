from pathlib import Path
from sys import path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from seleniumbase import Driver



path.append(Path(__file__).parent.as_posix())
pytest_plugins = []


@pytest.fixture(scope='module')
def driver():
    #driver = webdriver.Chrome()
    #driver.get('https://stroylandiya.ru')
    # initialize the driver in GUI mode with UC enabled
    driver = Driver(uc=True, headless=False)
    # set the target URL
    url = "https://stroylandiya.ru"
    # open URL using UC mode with 6 second reconnect time to bypass initial detection
    driver.maximize_window()
    driver.uc_open_with_reconnect(url, reconnect_time=10)
    # attempt to click the CAPTCHA checkbox if present
    driver.uc_gui_click_captcha()
    # close the browser and end the session
    yield driver
    driver.quit()
    driver.close()