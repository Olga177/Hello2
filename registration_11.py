# -*- coding UTF-8 _*_
# Create record (user account)

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


# 1. Creating object webdriver
driver = webdriver.Chrome()
# 2. Open the page
driver.get("http://localhost/litecart/en/login")
driver.implicitly_wait(30)
# 3. Find new customers link and click it
driver.find_element_by_css_selector("form[name=login_form]  a[href*=create_account]").click()
print("Headline", driver.find_element_by_tag_name("h1").text)

# 4. Populate required fields on Create Account page (in the form)
first_name = driver.find_element_by_name("firstname")
first_name.clear()
first_name.send_keys("Selenide")
last_name = driver.find_element_by_name("lastname")
last_name.clear()
last_name.send_keys("Python")
address1 = driver.find_element_by_name("address1")
address1.clear()
address1.send_keys("43d ave W")
postcode = driver.find_element_by_name("postcode")
postcode.clear()
postcode.send_keys("98199")
city = driver.find_element_by_name("city")
city.clear()
city.send_keys("Seattle")

# 4a. Find selector  option for country US
country_option_element = driver.find_element_by_css_selector("select.select2-hidden-accessible option[value*=US]")
print("country_selector_element = ",country_option_element)
country_option_element.click()

# 4b. Select state Washington from state (zone) selector
state_option_element = driver.find_element_by_css_selector("select[name=zone_code] option[value*=WA")
print("State_selector_element = ", state_option_element)
state_option_element.click()

# 4c. Populate remaining required fields
email = driver.find_element_by_name("email")
email.clear()
email.send_keys("pythonselenide@gmail.com")
phone = driver.find_element_by_name("phone")
phone.clear()
phone.send_keys("12063713288")
password = driver.find_element_by_name("password")
password.clear()
password.send_keys("selenide!&&")
confirmed_password = driver.find_element_by_name("confirmed_password")
confirmed_password.clear()
confirmed_password.send_keys("selenide!&&")

# 5. Find Create Account button and click it
submit_button = driver.find_element_by_css_selector("button[name*=create_account]")
print("Submit button found = ", submit_button)
submit_button.click()
driver.implicitly_wait(30)

# 6. Find OK button and click it
ok_button = driver.find_element_by_css_selector("button[name*=accept_cookies")
print("ok button found = ", ok_button)
ok_button.click()
driver.implicitly_wait(30)

# 7. Log out after account created
logout_element = driver.find_element_by_css_selector("div#box-account.box a[href*=logout]")
logout_element.click()
# 8. Check that user is logged out
print ("Headline Login is displayed on the page ", (driver.find_element_by_css_selector("h1")).text)

# 9 Populate email
email = driver.find_element_by_name("email")
email.clear()
email.send_keys("pythonselenide@gmail.com")

# 10. Populate password
password = driver.find_element_by_name("password")
password.clear()
password.send_keys("selenide!&&")

# 11. Click Login button
login_button = driver.find_element_by_css_selector("button[name*=login]")
print("Login button found = ", login_button)
login_button.click()
driver.implicitly_wait(30)

# 12. Log out
logout_element = driver.find_element_by_css_selector("div#box-account.box a[href*=logout]")
logout_element.click()
# 12a. Check that user is logged out
print ("Headline Login is displayed on the page ", (driver.find_element_by_css_selector("h1")).text)


#13.Close the page
driver.close()

#14.Close the browser
driver.quit()
