# -*- coding UTF-8 _*_
# Click each menu item and check if related page has headline
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

# 11. Find element - link for Countries
countries_menu = driver.find_element_by_css_selector("ul#box-apps-menu.list-vertical a[href*=countries]")
driver.implicitly_wait(20)
#print('menu item found')
current_href = countries_menu.get_attribute("href")
#print(current_href)

# 11a Click menu item to see page Countries
countries_menu.click()
#print("menu clicked")

#11b Find page headline
headline = driver.find_element_by_css_selector("h1").text
print("Headline found = ",headline)


#12c. Find  links to contries
country_links = driver.find_elements_by_css_selector("tr.row td a")
length = len(country_links)
#print("length =", length)
country_names =[]


#12d. Find contry names
for i in range(0,length,2):
    country_names.append(country_links[i].text)
#13 sort country names
sorted_country_names = sorted(country_names)
#13 Compare sorted and not sorted lists
countries_amount = len(country_names)
print("countries_amount =", countries_amount)
#print('sorted_country_names =', sorted_country_names)
#print("country names",country_names)
#print("sorted_country names2",sorted_country_names2)
j=0
for i in (range(countries_amount)) :
    if country_names[i] == sorted_country_names[i]:
        sorting_flag = 'true'
    else :
        print("Country names are not sorted for ", country_names[i], "(should be sd sorted_country_name ", sorted_country_names[i])

# 14 Find link to zones
geo_zones_menu = driver.find_element_by_css_selector("ul#box-apps-menu.list-vertical a[href*=geo_zones]")
driver.implicitly_wait(20)
# print('menu item found')
#current_href = countries_menu.get_attribute("href")
# print(current_href)

# 14a Click menu item to see page Geo Zones
geo_zones_menu.click()
# print("menu clicked")

# 14b Find page headline
headline = driver.find_element_by_css_selector("h1").text
print("Headline found = ", headline)

# 15 Find link to Canada zones
canadian_zones = driver.find_element_by_link_text("Canada")
#print("canadian zones", canadian_zones)
canadian_zones.click()
# 15a Find page headline
headline = driver.find_element_by_css_selector("h1").text
print("Headline found = ", headline)
#14b Find list of Canadian zones
canadian_zones_list = driver.find_elements_by_css_selector("select[name*=zone_code]")
print("Canadian_zones_list",canadian_zones_list)
canadian_zones_amount = len(canadian_zones_list)
print("canadian_zones_amount",canadian_zones_amount)

# 16 Find link to US zones page
# #us_zones = driver.find_element_by_link_text("United States of America")
# print("us zones", us_zones)
# us_zones.click()

#15a Find page headline
# headline = driver.find_element_by_css_selector("h1").text
# print("Headline found = ", headline)

#15b Find list of US zones
# us_zones_list = driver.find_elements_by_css_selector("select[name*=zone_code]")
# print("US_zones_list",us_zones_list)

# # 23. Close the page
# driver.close()

# 24. Close the browser
# driver.quit()