# -*- coding UTF-8 _*_
# Add products into the cart one by one. Remove products from the cart one by one.

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 1. Creating object webdriver
driver = webdriver.Chrome()

# 2. Open the page
driver.get("http://localhost/litecart/en/")

# 3. Set waiting time
driver.implicitly_wait(30)

# 4. Select product elements from Most Popular section, click one element to go to product page
for i in range(3):
     product_locator = "div#box-most-popular a[href*=p-"+str(i + 2)+"] div.image-wrapper img"
     # print("product locator = ", product_locator)
     product = driver.find_element_by_css_selector(product_locator)
     # print("product = ", product)
     product_title = product.get_attribute('alt')
     # print("product_title = ", product_title)
     product.click()
     driver.implicitly_wait(200)
     # print("product page displayed")
     # 4a. Find cart element and click it (wait when it becomes clicable)
     cart_locator = "td.quantity button[value*=Add]"
     cart_button = driver.find_element_by_css_selector(cart_locator)
     wait = WebDriverWait(driver, 20)
     wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, cart_locator)))
     cart_button.click()
     wait = WebDriverWait(driver, 20)
     element = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, cart_locator)))
     # 4b. Find amount of items in the cart and wait when it becomes  more by one
     locator = "a.content[href*=checkout] span.quantity"
     quantity_element = driver.find_element_by_css_selector(locator)
     quantity = quantity_element.text
     quantity_wait = str(i + 1)
     # print("quantity wait = ", quantity_wait)
     # 4c. Wait till quantity element is present
     wait = WebDriverWait(driver, 100)
     if quantity == str(i):
          # Note: 3 parameters in this kind of  wait
          quantity_element = wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, locator), quantity_wait))
     # print("ready to load home page =============")
     # 4d. Load home page
     driver.get("http://localhost/litecart/en/")
     driver.implicitly_wait(30)
     # print("total quantity = ", quantity_wait)

# 5. Get total quantity in the cart
total_quantity = int(quantity_wait)
print("total quantity = ", total_quantity)

# 6. Remove items from the cart one by one
for i in range(total_quantity):
     # 6a. Load home page
     driver.get("http://localhost/litecart/en/")
     driver.implicitly_wait(30)
     # 6b. Find cart element
     cart_button = driver.find_element_by_css_selector("div#cart a.image img")
     # print("cart button = ", cart_button)
     # print("cart button property = ", cart_button.get_attribute("src"))
     # 6c. Open cart page
     cart_button.click()
     driver.implicitly_wait(30)
     # 6d.  Remove  element and remove 1 item from the basket
     remove = driver.find_element_by_name("remove_cart_item")
     # print("remove", remove)
     # 6e. Remove one item from the cart
     remove.click()
     driver.implicitly_wait(30)
     print("One item removed")

# 7. Find of elements left in the cart
driver.get("http://localhost/litecart/en/")
driver.implicitly_wait(30)
locator = "a.content[href*=checkout] span.quantity"
quantity_element = driver.find_element_by_css_selector(locator)
quantity = quantity_element.text
print("quantity left", quantity)

