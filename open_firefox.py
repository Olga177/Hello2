# -*- coding UTF-8 _*_
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 1. Creating object webdriver for IE
driver = webdriver.Firefox()
print('Firefox 55.0 initiated (geckodriver -v0.18)')
driver.implicitly_wait(300)

# 2. Open the page
driver.get("http://www.theweathernetwork.com/weather/cabc0308")

# 3. Set waiting time
driver.implicitly_wait(3000)
print("Page opened in Firefox")

# 4. Close the page (for Firefox closes page and browser
driver.close()

# 5. Close the browser
# driver.quit()    this command gives an error in current scenario
