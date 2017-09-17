# -*- coding UTF-8 _*_
# Add new product and populate tabs: General, Prices, Information. Check if added product is in Catalog
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# 1. Creating object webdriver
driver = webdriver.Chrome()

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

#12.Find Add new product button and click it
driver.find_element_by_css_selector("a.button[href*=edit_product]").click()

# 13. Find status element of type = radio and value = 1 (Enabled) and click it
driver.find_element_by_xpath("//*[contains(@value,'1') and contains(@type,'radio')]").click()
# print("status clicked")

name = driver.find_element_by_name("name[en]")
name.clear()
new_product_name  ='Pink Duck'
name.send_keys(new_product_name)

code = driver.find_element_by_name("code")
code.clear()
code.send_keys("3625")

# 13a. Find Categories set of checkboxes
driver.find_element_by_css_selector("input[type=checkbox][data-name*=Root]").click()
driver.find_element_by_css_selector("input[type=checkbox][data-name*=Rubber]").click()



# # 13b. Find checkbox for Product Groups
product_group = driver.find_element_by_xpath("//*[contains(@value,'1-2')]")
# # print("Gender_chebox_element is found", product_group)
product_group.click()
#
# # 13c. Find Quantity  Selector
quantity = driver.find_element_by_name("quantity")
driver.implicitly_wait(5)
# # print("quantity size =", quantity.size) # 32  120
# Clicking on the element quantity with offset to click on little arrow
for i in range (20):
    ActionChains(driver).move_to_element_with_offset(quantity, 109, 14).click().perform() # quantity number dispalyed
    driver.implicitly_wait(1)

#13d. Find input file element
driver.find_element_by_xpath("//*[contains(@name,'new_images[]')]").send_keys(".\\pink_duck.jpg")

#13e. Find element Data Valid From - Calendar  and set up date
data_from = driver.find_element_by_css_selector("input[name*=from]")
# print("data from", data_from)
data_from.send_keys("09/09/2017")
# ActionChains(driver).move_to_element_with_offset(data_from, 165, 17).click().perform()  #Calendar opened


#13f. Find element Data Valid To - Calendar
data_to = driver.find_element_by_css_selector("input[name*=date_valid_to]")
# print("element data valid to found",data_to)
data_to.send_keys("12/09/2017")

# 14. Find tab -------------  Prices ------------------- and click it
driver.find_element_by_css_selector("a[href*=tab-prices]").click()
driver.implicitly_wait(20)

# 14a. Find selector Purchase price and select amount
purchase_price = driver.find_element_by_name("purchase_price")
# print("purchase_price element size =", purchase_price)
for i in range (10):
    ActionChains(driver).move_to_element_with_offset(purchase_price, 109, 14).click().perform()

driver.find_element_by_css_selector("select[name*=purchase_price_currency_code] option[value*=USD]").click()

# 14b. Find selector tax class and select tax class
price_with_tax = driver.find_element_by_name("gross_prices[USD]")
for i in range (11):
    ActionChains(driver).move_to_element_with_offset(price_with_tax, 109, 14).click().perform()

# 15. Find tab -------- Information ----------  and click it
driver.find_element_by_css_selector("a[href*=tab-information]").click()
driver.implicitly_wait(20)

# 15a. Find selector Manufacturer and select amount
driver.find_element_by_css_selector("select[name*=manufacturer_id] option:last-child").click()

# 15b. Find element for  Keywords  and enter text
keywords = driver.find_element_by_name("keywords")
keywords.clear()
keywords.send_keys("Safe_toy")

# 15c. Find element Short Description and enter text
short_description = driver.find_element_by_xpath("//*[contains(@name,'short_description[en]')]")
# print("short description", short_description)
ActionChains(driver).move_to_element_with_offset(short_description, 35, 5).click().perform()
short_description.clear()
short_description.send_keys("Safe, swims, bright")


# 15d. Find element Description and enter text
text_to_enter = "Safe, smooth and  bright toy for babies to play in the water"
element = driver.find_element_by_css_selector("div[dir*=ltr]").click()
element = driver.switch_to.active_element
element.send_keys(text_to_enter)


# 15e. Find field Head Title  and enter text
head_title = driver.find_element_by_name("head_title[en]")
ActionChains(driver).move_to_element_with_offset(head_title, 35, 5).click().perform()
head_title.clear()
head_title.send_keys(new_product_name)

# 15g. Find field Meta Description  and enter text
meta_description= driver.find_element_by_name("meta_description[en]")
ActionChains(driver).move_to_element_with_offset(meta_description, 35, 5).click().perform()
meta_description.clear()
meta_description.send_keys(new_product_name)

# 16. Find button save and click it
driver.find_element_by_css_selector("button[type=submit][name=save]").click()
driver.implicitly_wait(30)

# 17. Check that new added product is in Catalog
# 17a.  Go to admin page
driver.get("http://localhost/litecart/admin/")

# 17b.  Find element and click Catalog menu
driver.find_element_by_css_selector("ul#box-apps-menu.list-vertical li#app- a[href*=catalog]").click()

#17c. Find search field element
query = driver.find_element_by_name("query")
# print("query element = ", query)

# 17d.  Enter text by send_keys and click Enter
query.send_keys(new_product_name + Keys.ENTER)

# 17e. Find element with amount of search results
amount = driver.find_element_by_css_selector("form[name= catalog_form] table.dataTable td").text
#  print("amount = ", amount)
# 17f. Check that new added product is in catalog
if amount == 'Products: 0':
    print("Error: New added product", new_product_name, " is not in Catalog")

# 18. Close the page
driver.close()

# 19. Close the browser
driver.quit()