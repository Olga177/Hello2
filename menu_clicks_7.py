# -*- coding UTF-8 _*_
# Click each main menu item and then click related sub menu items if any of them exist. Check if related page has headline with tag h1
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

# 11. Find elements to help searching for basic  menu
basic_menu = driver.find_elements_by_css_selector("ul#box-apps-menu.list-vertical li#app- a")
driver.implicitly_wait(20)
basic_menu_length = len(basic_menu)
print("Amount of items in main menu = ", basic_menu_length)

# 12. Find basic menu elements
for j in range(basic_menu_length):
    # 12a. Refresh admin page
    driver.get("http://localhost/litecart/admin/")
    # 12b. Find elements of basic menu
    basic_menu = driver.find_elements_by_css_selector("ul#box-apps-menu.list-vertical li#app- a")
    # 12c. Find name of basic menu item
    basic_menu_name = basic_menu[j].text
    # 12d. Click basic menu item and check if page has tag h1
    basic_menu[j].click()
    h1_elements = driver.find_elements_by_css_selector("h1")
    headline_length = len(h1_elements)
    if headline_length == 0 :
        print("Error: No headline with tag h1 for main menu item ", basic_menu_name)
    else :
        print("Headline is ", h1_elements[0].text," for main menu item ", basic_menu_name)

    # 13. Find sub menu elements and sub menu length
    sub_menu_items = driver.find_elements_by_css_selector("ul.docs a")
    sub_menu_length = len(sub_menu_items)
    print("Amount of items in sub menu = ", sub_menu_length)
       # 13a. Find sub menue elements when they are exist (when sub_menu_length >0)
    if sub_menu_length > 0:
        for i in range(sub_menu_length):
            # 13d. Refresh main menu elements and sub menu elements before next iteration
            main_menu_items = driver.find_elements_by_css_selector("ul#box-apps-menu.list-vertical li#app- a")
            main_menu_items[j].click
            sub_menu_items = driver.find_elements_by_css_selector("ul.docs a")
            sub_menu_item = sub_menu_items[i]
            # 13b. Find sub menu element name
            sub_menu_name = sub_menu_item.text
            # 13c. Click sub menu item and check if page has tag h1
            sub_menu_item.click()
            h1_elements = driver.find_elements_by_css_selector("h1")
            headline_length = len(h1_elements)
            if headline_length == 0:
                print("Error: No headline with tag h1 for sub menu item ", sub_menu_name)
            else:
                print("Headline is ", h1_elements[0].text, " for sub menu item ", sub_menu_name)
            # 13d. Refresh main menu elements and sub menu elements before next iteration
            # main_menu_items = driver.find_elements_by_css_selector("ul#box-apps-menu.list-vertical li#app- a")
            # main_menu_items[j].click
            # sub_menu_items = driver.find_elements_by_css_selector("ul.docs a")



# 14. Close the page
driver.close()

# 15. Close the browser
driver.quit()