# -*- coding UTF-8 _*_
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 1. Creating object webdriver for IE
driver = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Nightly\\firefox.exe")
print('Firefox nightly initiated (geckodriver -v0.18)')
driver.implicitly_wait(300)

# 2. Open the page
driver.get("http://www.theweathernetwork.com/weather/cabc0308")

# 3. Set waiting time
driver.implicitly_wait(3000)
print("Page opened in Firefox")


