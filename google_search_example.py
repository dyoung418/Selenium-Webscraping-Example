import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def init_browser(timeout=10):
    # Specifying incognito mode as you launch your browser[OPTIONAL]
    option = webdriver.ChromeOptions()
    option.add_argument("--incognito")
    option.add_argument("--headless")

    # Create new Instance of Chrome in incognito mode
    browser = webdriver.Chrome(executable_path='./chromedriver', options=option)
    browser.wait = WebDriverWait(browser, timeout)
    return browser

def google_search(browser, query):
    browser.get("https://www.google.com")
    try:
        box = browser.wait.until(EC.presence_of_element_located(
            (By.NAME, "q")))
        #        button = browser.wait.until(EC.element_to_be_clickable(
        #    (By.NAME, "btnK")))
        box.clear()
        box.send_keys(query)
        box.send_keys(Keys.RETURN)
        #button.click()
        try:
            browser.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id='rso']/div[@class='bkWMgd'][h2='Web results'][1]")))
            results_elements = browser.find_elements_by_xpath("//*[@id='rso']/div[@class='bkWMgd'][h2='Web results'][1]")
            print("First result: {}".format(results_elements[0].text))
        except TimeoutException:
            print("Timed out waiting for search result")
            browser.quit()
    except TimeoutException:
        print("Google's search box or button not found")
        browser.quit()

if __name__ == "__main__":
    try:
        browser = init_browser()
        google_search(browser, "selenium")
        time.sleep(5)
    finally:
        pass
        if browser:
            browser.quit()
