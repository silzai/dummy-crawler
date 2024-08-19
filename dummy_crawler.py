from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait    
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import random

def setup_chromedriver():
    # setting up selenium
    # service = webdriver.ChromeService(executable_path="/usr/bin/chromedriver/chromedriver")
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--ignore-certificate-errors')
    #options.add_argument("--test-type")
    options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument('--disable-gpu') if os.name == 'nt' else None # Windows workaround
    options.add_argument("--verbose")
    options.add_argument('--disable-notifications')
    options.add_argument('--lang=en-GB')
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})

    return webdriver.Chrome(options = options)

def get_page_source(driver : webdriver.Chrome, url):

    driver.get(url)

    element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
    element.click()
    time.sleep(random.uniform(0.5, 2))
    content = element.get_attribute('outerHTML')
    return content

def main():

    driver = setup_chromedriver()

    os.makedirs('./output', exist_ok=True)

    url = 'http://example.com/'

    for i in range(10):
        content = get_page_source(driver, url)
        with open(f"./output/{i}.html", 'w', encoding="utf-8") as f:
                f.write(f"{content}")
	
    driver.close()

if __name__ == "__main__":
    main()
