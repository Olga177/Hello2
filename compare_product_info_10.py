# -*- coding UTF-8 _*_
# Check that product name and prices are identical

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def isItRed (values):  # Check if the color is red - if all 3 parameters are the same
    if values[1] == values[2]:
        if values[1] == values[3]:
            result = True
        else:
            result = False
    else:
        result = False
    return result

def isItGray(values):  # Check if the color is gray - if only last 2 parameters are the same
    if values[1] == values[2]:
        result = False
    else:
        if values[1] == values[3]:
            result = True
        else:
            result = False
    return result


def colorComponents(rgba_value):
    # Selecting  3 color components from rgba_value into values like: 123
    start = rgba_value.index("(")
    end = rgba_value.index(")")
    rgba_value = rgba_value[start + 1: end]  # rgba_value is now like "123, 123, 123, 1")
    values = rgba_value.split(",")  # Splitting string into array
    values = [int(x.strip()) for x in
              values]  # Trimming values to get rid of whitespace and converting strings to integers

    return values


# 1. Creating object webdriver
driver = webdriver.Chrome()
# 2. Open the page
driver.get("http://localhost/litecart/en/")
driver.implicitly_wait(30)

# 3. Find product on Home page and save product name,  regular price and campaign price for this product
# 3a. Find product name on the Home page
product_name = driver.find_element_by_css_selector("div#box-campaigns.box a.link div.name").text
driver.implicitly_wait(20)
print('Product name = ', product_name)

# 4. Find  regular price element and retain the amount,  text decoration, color and font size
regular_price_element = driver.find_element_by_css_selector("div#box-campaigns.box a.link div.price-wrapper s.regular-price")
regular_price_amount = (regular_price_element).text
regular_price_decoration = (regular_price_element).value_of_css_property("text-decoration")
regular_price_color = (regular_price_element).value_of_css_property("color")
regular_price_font_size = (regular_price_element).value_of_css_property("font-size")
driver.implicitly_wait(20)
print('regular price amount = ', regular_price_amount)
print("regular price decoration = ", regular_price_decoration)
print("regular price color = ", regular_price_color)
print("regular price font size = ", regular_price_font_size)
# 4a. Parse value for regular price color
values = colorComponents(regular_price_color)
print("after calling colorComponents =", values)

# 4b. Check if regular price is gray
if isItGray(values):
    print('On Home page regular price color is gray')
else:
    print('Error: On home page regular color is not gray')

#4c Check if regular price text decoration is line-through
text_decoration = 'line-through'
if text_decoration in regular_price_decoration :
    print("Text decoration is line-through")
else:
    print("Error: On home page text-decoration for regular price is not line-through" )

# 4c. Find product campaign price, text decoration, color and font size
campaign_price_element =driver.find_element_by_css_selector("div#box-campaigns.box a.link strong.campaign-price")
campaign_price = campaign_price_element.text
campaign_price_decoration =(campaign_price_element).value_of_css_property("text-decoration")
campaign_price_text_weight =(campaign_price_element).value_of_css_property("font-weight")
campaign_price_color = (campaign_price_element).value_of_css_property("color")
campaign_price_font_size = (campaign_price_element).value_of_css_property("font-size")
print("campaign price = ",campaign_price)
print("campaign price decoration = ",campaign_price_decoration)
print("campaign price color = ",campaign_price_color)
print("campaign price weight = ",campaign_price_text_weight)
print("campaign price font size = ",campaign_price_font_size)

# 5. Checks
# 5a. Check if regular price font size less then campaign price font size
if regular_price_font_size >= campaign_price_font_size :
    print('Error: On home page font size of regular price of the product ',product_name," should be  les than ",campaign_price_font_size )

#5b Check if campaign price text decoration is bold
if campaign_price_text_weight != 'bold':
    print("Error: On Home page campaign price text decoration is not bold")

# 5c. Check that campaign price is red
values1 = colorComponents(campaign_price_color)
# print("For campaign price - after calling colorComponents =", values1)
if isItRed(values1):
    print('Error: campaign price color is not red')
else:
    print('Campaign price color is red')

print ("Checks on Home page are over ====================================================")
# # 7. Check values on product page
# 7a. Click product on home page to go to product page
driver.find_element_by_css_selector("div#box-campaigns.box a.link div.name").click()

# # 8. Find product campaign price, text decoration, color and font size
# # 8a. Find product name
product_name2 = driver.find_element_by_css_selector("h1").text
driver.implicitly_wait(20)
print('Product name on product page = ', product_name2)

# # 9. Find product regular price
regular_price_element2 = driver.find_element_by_css_selector("div.information s.regular-price")
regular_price2 = (regular_price_element2).text
regular_price_decoration2 = (regular_price_element2).value_of_css_property("text-decoration")
regular_price_color2 = (regular_price_element2).value_of_css_property("color")
regular_price_font_size2 = (regular_price_element2).value_of_css_property("font-size")
driver.implicitly_wait(20)
print('regular price 2 = ', regular_price2)
print("regular price decoration 2 = ", regular_price_decoration2)
print("regular price color 2 = ", regular_price_color2)
print("regular price fonf size 2 = ", regular_price_font_size2)
# 9a. Check parameters of regular price on Product page
# 9b. Check if regular price is gray
values3 = colorComponents(regular_price_color2)
if isItGray(values3):
    print('On Home page regular price color is gray')
else:
    print('Error: On home page regular color is not gray')

# 9c Check if regular price text decoration is line-through
if text_decoration in regular_price_decoration2:
    print("Text decoration is line-through")
else:
    print("Error: On home page text-decoration for regular price is not line-through")
print ("Checks for regular  price on Product page are over ====================================================")
# 10. Find product campaign price, text decoration and text color on Product page
campaign_price_element2 = driver.find_element_by_css_selector("div.information strong.campaign-price")
campaign_price2 = campaign_price_element2.text
campaign_price_decoration2 =(campaign_price_element2).value_of_css_property("text-decoration")
campaign_price_text_weight2 =(campaign_price_element2).value_of_css_property("font-weight")
campaign_price_color2 = (campaign_price_element2).value_of_css_property("color")
campaign_price_font_size2 = (campaign_price_element2).value_of_css_property("font-size")
print("campaign price2 = ",campaign_price2)
print("campaign price decoration 2= ",campaign_price_decoration2)
print("campaign_price_text_weight2= ",campaign_price_text_weight2)
print("campaign price color 2= ",campaign_price_color2)
print("campaign price fonf size 2 = ",campaign_price_font_size2)



# # 10a Checks for campaign price on Product page
#5b Check if campaign price text decoration is bold
# if campaign_price_text_weight2 != 'bold':
#     print("Error: On Home page campaign price text decoration is not bold")

# 5c. Check that campaign price is red
values4 = colorComponents(campaign_price_color2)
#print("For campaign price - after calling colorComponents =", values4)
if isItRed(values4):
    print('Error: campaign price color is not red')
else:
    print('Campaign price color is red')


# # 11. Check that product names on home page and product page are the same
if product_name != product_name2  :
    print ("Error: Product names are different. On Home page Product name = ",product_name," on Product page Product name = ",product_name2)

# # 12. Check that product regular price on home page and product page are the same
if regular_price_amount != regular_price2:
    print("Error: Regular prices are different. On Home page regular price =",regular_price," on Product page regular price = ",regular_price2)

# # 13. Check that product regular price on home page and product page are the same
if campaign_price != campaign_price2:
    print("Error: Campaign prices are different. On Home page campaign price = ",campaign_price," on Product page campaign price = ",campaign_price2)



# 20. Close the page
# driver.close()

# 21. Close the browser
# driver.quit()

