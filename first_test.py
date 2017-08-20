# -*- coding UTF-8 _*_
import os
from selenium import webdriver

#1. Creating object webdriver
driver = webdriver.Chrome()

# 2. Open the page
driver.get("https://www.theweathernetwork.com")

# 3. Set waiting time
driver.implicitly_wait(30)

# 4. Close the page
driver.close()
driver.quit()
