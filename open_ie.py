# -*- coding UTF-8 _*_
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 1. Creating object webdriver for IE
driver = webdriver.Ie()
print('IE initiated')
driver.implicitly_wait(300)
# 2. Open the page
driver.get("http://www.theweathernetwork.com/weather/cabc0308")

# 3. Set waiting time
# driver.implicitly_wait(300)
print("IE opened")

# 4. Close the page
# driver.close()

# 5. Close the browser
# driver.quit()
# ("C:\\Python36\\IEDriverServer.exe")