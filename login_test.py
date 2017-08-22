# -*- coding UTF-8 _*_
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
print("Username typed")

# 6. Find element  with name "password"
password = driver.find_element_by_name("password")

# 7. Type password
password.clear()
password.send_keys("admin")
print("Password entered")

# 8. Find element Login
login = driver.find_element_by_name("login")

# 9. Click button Login
login.click()
print("Login clicked")

# 10. Set waiting time
driver.implicitly_wait(2000000)

# 11. Close the page
driver.close()

# 12. Close the browser
driver.quit()