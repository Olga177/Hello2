# -*- coding UTF-8 _*_
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 1. Creating object webdriver for IE
driver = webdriver.Firefox(capabilities={"marionette": False})
print('Firefox ESR45 initiated')
driver.implicitly_wait(300)

# 2. Open the page
driver.get("http://www.theweathernetwork.com/weather/cabc0308")

# 3. Set waiting time
driver.implicitly_wait(3000)
print("Page opened in Firefox")

# 4. Close the page (for Firefox closes page and browser
driver.close()