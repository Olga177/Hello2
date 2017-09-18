# -*- coding UTF-8 _*_
# Check that on editing country clicking icons open new windows
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


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

# 11. Click on the menu Countries
driver.find_element_by_css_selector("ul#box-apps-menu.list-vertical li#app- a[href*=countries]").click()
# 11a. Find add new country button and click it
driver.find_element_by_css_selector("a.button").click()


def check_opening_and_closing_new_window(locator):
    # 12. Checks if clicking the link by locator opens and closes external window correctly
    # 12a. Check open windows and current window for Add New Country page
    driver.get("http://localhost/litecart/admin/?app=countries&doc=edit_country")
    driver.implicitly_wait(200)

    # 12b. Find current window id and opened windows ids
    current_window_before_click = driver.current_window_handle
    # print("   current window before click = ", current_window_before_click)
    all_windows_before_click = driver.window_handles
    # print("   all windows before click = ", all_windows_before_click)

    # 12c Find element that will be clicked
    element = driver.find_element_by_css_selector(locator)
    # print("element = ", element)
    # Print the link for element that will be clicked
    print("Link for the page that will be opened =", element.get_attribute("href"))

    # 12cd. Click on icon with arrow (per locator)
    driver.find_element_by_css_selector(locator).click()
    driver.implicitly_wait(300)

    # 12d.Check that after  new window opened, current window did not change
    current_window_after_click = driver.current_window_handle
    # print("   current window after click = ", current_window_after_click)
    all_windows_after_click = driver.window_handles
    # print("   all windows after click = ", all_windows_after_click)
    # 13. Find id for new opened window
    if current_window_before_click != current_window_after_click:
        print("Error: Current window changed after clicking icon ")
    else:
        # 13a. Find id for new opened window
        amount_of_open_windows = len(all_windows_after_click)
        print("Amount of opened windows = ", amount_of_open_windows)
        for i in range(amount_of_open_windows):
            window_element = all_windows_after_click[i]
            if window_element != current_window_before_click:
                window_to_switch_to = window_element
                # print("   window_to_go = ", window_to_switch_to)
                # 14. Switch to new opened window
                driver.switch_to_window(window_to_switch_to)
                # print("   Opened new window with title = ", driver.find_element_by_css_selector("h1").text)
                # 15. Close new window where we are now
                driver.close()
                driver.implicitly_wait(300)
                # print("New window closed")

    driver.switch_to_window(current_window_before_click)
    # print("   switching back to first window = ", current_window_before_click)

    # 16. Find what window is current
    current_window_after_closing = driver.current_window_handle  # Error here
    # print("   Current window after closing = ", current_window_after_closing)
    if current_window_after_closing != current_window_before_click:
        print("Error: Current window changed after closing opened window ")
        return
    else:
        return

# 17. Check for windows with specific locators (windows openen by clicking icons)
check_opening_and_closing_new_window("a[href*=alpha-2]")  # Code alpha-2

check_opening_and_closing_new_window("a[href*=alpha-3]")  # Code alpha-3
check_opening_and_closing_new_window("a[href*=Regular_expression]")  # Tax id format
check_opening_and_closing_new_window("a[href*=address-formats]")  # Address Format
check_opening_and_closing_new_window("a[href*=Regular_expression]")  # Postcode Format
check_opening_and_closing_new_window("a[href*=currency]")  # Currency Code
check_opening_and_closing_new_window("a[href*=calling]")  # Phone Country Code


# 18. Close the page
driver.close()

# 19. Close the browser
driver.quit()



