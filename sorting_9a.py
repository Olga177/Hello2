# -*- coding UTF-8 _*_
# Check if countries and zones are sorted
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def compareArrays (length,country_names,sorted_country_names): # Compare sorted and unsorted string arrays of the same length
    for i in (range(length)):
        if country_names[i] != sorted_country_names[i]:
            print("Names are not sorted for ", country_names[i], "(should be as sorted_names ",
                  sorted_country_names[i])

# 1. Creating object webdriver
driver = webdriver.Chrome()

# 2. Open the  page to log in into admin
driver.get("http://localhost/litecart/admin/")
# 2a. Set waiting time
driver.implicitly_wait(30)
# 2b.Find element with name "username"
username = driver.find_element_by_name("username")
# 2c. Type  username
username.clear()
username.send_keys("admin")
# 2d. Find element  with the name "password"
password = driver.find_element_by_name("password")
# 2e. Type password
password.clear()
password.send_keys("admin")
# 2f. Find element Login
login = driver.find_element_by_name("login")
# 2g. Click button Login
login.click()
# 2i. Set waiting time
driver.implicitly_wait(20)

# 3. Check that Country Names are sorted on Country page
# 3a. Find element - link for Countries
countries_menu = driver.find_element_by_css_selector("ul#box-apps-menu.list-vertical a[href*=countries]")
driver.implicitly_wait(20)
#print('menu item found')
# 3b. Click Countries menu item to see page Countries
countries_menu.click()
#print("menu clicked")
# 3c. Find page headline to be sure that page name is Countries
headline = driver.find_element_by_css_selector("h1").text
print("Headline found = ",headline)


# 4. Find  links to all contries on Contries page
country_links = driver.find_elements_by_css_selector("tr.row td a")  # Only odd elements are correct, even elements are not related
amount_of_countries = len(country_links)
print("Amount_of_countries = ", amount_of_countries)


# 5. Find country names and put them in country_names (skipping even elements in country_links)
country_names =[]
for i in range(0,amount_of_countries,2):
    country_names.append(country_links[i].text)
# 5a. Sort country names
sorted_country_names = sorted(country_names)

# 6. Compare sorted and not sorted lists
countries_amount = len(country_names)
print("Countries_amount =", countries_amount)
#print('sorted_country_names =', sorted_country_names)
#print("country names",country_names)
compareArrays(countries_amount,country_names, sorted_country_names)

# 7. Find link to zones
geo_zones_menu = driver.find_element_by_css_selector("ul#box-apps-menu.list-vertical a[href*=geo_zones]")
driver.implicitly_wait(20)
# print('menu item found')
# 7a. Click menu item to see page Geo Zones
geo_zones_menu.click()
# print("menu clicked")
# 7b. Find page headline
headline = driver.find_element_by_css_selector("h1").text
print("Headline found = ", headline)

# 8 Find link to Canadian zones
canadian_zones = driver.find_element_by_link_text("Canada")
#print("canadian zones", canadian_zones)
# 8a. Go to the page with Canadian zones
canadian_zones.click()
# 8b.  Find page headline
headline = driver.find_element_by_css_selector("h1").text
print("Headline found = ", headline)
# 8c. Find list of Canadian zones
canadian_zones_list = driver.find_elements_by_css_selector("select[name*=zone_code] option[selected*=selected]")
#print("Canadian_zones_list",canadian_zones_list)
# 8d. Find amount of Canadian zones
canadian_zones_amount = len(canadian_zones_list)
print("Canadian_zones_amount",canadian_zones_amount)

# 9. Find Canadian zone names
canadian_zones_names =[]
for i in range(canadian_zones_amount):
    canadian_zones_names.append(canadian_zones_list[i].text)
# print("Canadian_zones_names",canadian_zones_names)

# 10. Sort Canadian zones names
sorted_canadian_zones_names = sorted(canadian_zones_names)
# print("Sorted Canadian_zones_names",sorted_canadian_zones_names)

# 11. Check that zone names are sorted
compareArrays(canadian_zones_amount,canadian_zones_names, sorted_canadian_zones_names)

# 12 Checking if US zone names are sorted
# 12a. Find link to geo-zones page
geo_zones_menu = driver.find_element_by_css_selector("ul#box-apps-menu.list-vertical a[href*=geo_zones]")
driver.implicitly_wait(20)
# 12b. Go to the gep-zones page
geo_zones_menu.click()
# 12c. Find page headline
headline = driver.find_element_by_css_selector("h1").text
print("Headline found = ", headline)

# 13. Find  a link to   US zones
us_zones = driver.find_elements_by_css_selector("table.dataTable tr.row a[href*=id]")[2]
print ("US link = ", us_zones.text)
#print("us zones", us_zones)
# 13a. Go to the page with  US zones
us_zones.click()

# 14. Find list of US zones
us_zones_list = driver.find_elements_by_css_selector("select[name*=zone_code] option[selected*=selected]")
#print("US_zones_list",us_zones_list)
# 14a. Find amount of US zones
us_zones_amount = len(us_zones_list)
print("US_zones_amount",us_zones_amount)

# 15. Find US zone names
us_zones_names =[]
for i in range(us_zones_amount):
    us_zones_names.append(us_zones_list[i].text)
#print("US_zones_names",us_zones_names)

# 15a. Sort US zones names
sorted_us_zones_names = sorted(us_zones_names)
#print("Sorted UD_zones_names",sorted_us_zones_names)

# 16. Check that zone names are sorted
compareArrays(us_zones_amount,us_zones_names, sorted_us_zones_names)




# 17. Close the page
driver.close()

# 18. Close the browser
driver.quit()