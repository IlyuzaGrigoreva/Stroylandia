import undetected_chromedriver as uc
from time import sleep

if name == "__main__":
    driver = uc.Chrome(
        use_subprocess=False,
        headless=True,
    )
    driver.get("https://stroylandiya.ru/cart")
    sleep(10)
    driver.quit()