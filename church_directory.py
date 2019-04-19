from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Specifying incognito mode as you launch your browser[OPTIONAL]
option = webdriver.ChromeOptions()
#option.add_argument("--incognito")
#option.add_argument("--headless")  # don't use this since I have to manually log in

# Create new Instance of Chrome in incognito mode
browser = webdriver.Chrome(executable_path='./chromedriver', chrome_options=option)

#############################################
#  Log into Leaders and Clerk's Resources
#############################################

# Go to website
browser.get("https://www.lds.org/mls/mbr/?lang=eng") # Leaders and Clerks resources

# Wait 30 seconds for page to load  (I will need to manually log in first)
timeout = 30
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="heading-unit-name"]')))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()
finally:
    pass

#############################################
#  Get Members with Callings List
#############################################
try:
    # First, go to members with callings list
    # Go to desired website
    browser.get("https://lcr.lds.org/orgs/members-with-callings?lang=eng") # Members with Callings
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pageTitleText"]')))


    # find_elements_by_xpath - Returns an array of selenium objects.
    table_rows = browser.find_elements_by_xpath('//*[@id="mainContent"]/table/tbody/tr')
    
    # List Comprehension to get the actual repo titles and not the selenium objects.
    members_with_callings = []
    for x in table_rows:
        name_link = x.find_element_by_xpath('td[2]/member-card/a/ng-transclude/span') #note this is singular element
        gender = x.find_element_by_xpath('td[3]')
        age = x.find_element_by_xpath('td[4]')
        birthdate = x.find_element_by_xpath('td[5]')
        organization = x.find_element_by_xpath('td[6]')
        calling = x.find_element_by_xpath('td[7]')
        sustained = x.find_element_by_xpath('td[8]')
        members_with_callings.append([name_link.text, gender.text, age.text, birthdate.text,
                                    organization.text, calling.text, sustained.text])
    for entry in members_with_callings:
        print(','.join(entry))
        print('')
    
except:
    raise
finally:
    browser.quit()
