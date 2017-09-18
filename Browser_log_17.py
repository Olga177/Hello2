# -*- coding UTF-8 _*_
# Check any messages in browser log when opening product pages  for items in  Catalog
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.support.events import AbstractEventListener
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



# 1. Creating object webdriver
# driver = webdriver.Chrome()

# 1a. Enable browser logging
d = DesiredCapabilities.CHROME
d['loggingPrefs'] = { 'browser':'ALL' }
driver = webdriver.Chrome(desired_capabilities=d)

# 2. Open the page
driver.get("http://localhost/litecart/admin/")

# 3. Set waiting time
driver.implicitly_wait(30)

# 4.Find element with name "username"
username = driver.find_element_by_name("username")

# 5. Type  username
username.clear()
username.send_keys("admin")

# 6. Find element  with name "password"
password = driver.find_element_by_name("password")

# 7. Type password
password.clear()
password.send_keys("admin")

# 8. Find element Login
login = driver.find_element_by_name("login")

# 9. Click button Login
login.click()

# 10. Set waiting time
driver.implicitly_wait(20)

# # 11. Find element for Catalog menu and click it
driver.find_element_by_css_selector("ul#box-apps-menu.list-vertical li#app- a[href*=catalog]").click()

# 12 Find element for search, enter value, click
search_element = driver.find_element_by_css_selector("input[type=search][name=query]")
# print("search element = ", search_element)
search_element.clear()
# print("after clearing search element")
search_element.send_keys("Duck" + Keys.ENTER)
# print("after populating inding search result")

# 14. Find all products
products_links = driver.find_elements_by_css_selector("form[name=catalog_form] a[href*=product]")
# print("product links",products_links)
length_of_product = len(products_links)
print("lenght of product links", length_of_product)

# 15. Click each product to go to product page
for i in range(0,length_of_product,2):
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=0&query=Duck")
    products_links = driver.find_elements_by_css_selector("form[name=catalog_form] a[href*=product]")
    product = products_links[i]
    print("product", product.text)
    product.click()

# 16. Print messages from log
for entry in driver.get_log('browser'):
    print(entry)

# 17. Close the page
driver.close()

# 18. Close the browser
driver.quit()