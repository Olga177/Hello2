# -*- coding UTF-8 _*_
# Check that all goods displayed on home page have only one sticker

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 1. Creating object webdriver
driver = webdriver.Chrome()

# 2. Open the page
driver.get("http://localhost/litecart/en/")

# 3. Set waiting time
driver.implicitly_wait(30)

# 4a. Find elements with alt ='Purple Duck'
# purple_ducks = driver.find_elements_by_css_selector("img[alt*=Purple")

# 4b. Find links for all  Purple Duck products
purple_ducks = driver.find_elements_by_css_selector("li.hover-light a.link[title*=Purple]")
driver.implicitly_wait(20)
amount_of_purple_products = len(purple_ducks)
# print("Amount of purple products = ",amount_of_purple_products)

# 4c. Find amount of stickers for each purple product
for i in range(amount_of_purple_products):
    purple_product = purple_ducks[i]
    purple_product_name = purple_product.get_attribute("title")
    # print("Purple product name = ",purple_product_name)
    # print("Purple product = ",purple_product)
    # 4d. Find all stickers for the purple product
    purple_stickers = purple_product.find_elements_by_css_selector("div.sticker")
    # print("Purple stickers = ", purple_stickers)
    # 4e. Find amount of stickers for particular purple product
    amount_of_purple_stickers = len(purple_stickers)
    print("Amount of stickers for purple product", (i + 1), " = ", amount_of_purple_stickers)
    if amount_of_purple_stickers == 0:
        print("Error: Product ", purple_product_name, "has no sticker")
    else:
        if amount_of_purple_stickers > 1:
            print("Error: Product ", purple_product_name, " has more than one sticker")

# 5. Find link elements for all products on the Home page
products = driver.find_elements_by_css_selector("li.hover-light a.link")
driver.implicitly_wait(20)
# 5a. Find amount of products
amount_of_products = len(products)
print("Amount of products = ", amount_of_products)
# print('Products found', products)
# 5a. Find amount of stickers for all products on Home page
for i in range(amount_of_products):
    product = products[i]
    product_name = product.get_attribute("title")
    print("Product", (i + 1), "name = ", product_name)
    # print("Product",(i + 1)," = ", product)
    # 5b. Find all stickers for particular product
    stickers = product.find_elements_by_css_selector("div.sticker")
    # print("Stickers", stickers)
    # 5c. Find amount of stickers for particular product
    amount_of_stickers = len(stickers)
    print("Amount of stickers for product", (i + 1), " = ", amount_of_stickers)
    if amount_of_stickers == 0:
        print("Error: Product ", product_name, "has no sticker")
    else:
        if amount_of_stickers > 1:
            print("Error: product ", product_name, " has more than one sticker")

#6.Close the page
driver.close()

#7.Close the browser
driver.quit()
