import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

k_timeout = 10

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_argument("--incognito")
        #option.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=option)
        self.driver.implicitly_wait(k_timeout) #waits on any find implicitly, without WebDriverWait

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
