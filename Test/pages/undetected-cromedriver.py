import undetected_chromedriver as uc
from time import sleep

if name == "__main__":
    # instantiate a Chrome browser
    driver = uc.Chrome(
        use_subprocess=False,
        headless=True,
    )

    # visit the target page
    driver.get("https://stroylandiya.ru/cart")

    # wait for the interstitial page to load
    sleep(10)

    # take a screenshot of the current page and save it
    driver.save_screenshot("cloudflare-challenge.png")

    # close the browser
    driver.quit()