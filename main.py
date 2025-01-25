from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
# from Login import login
# from Sort import sort

# Task 1: Login Validation : 
# login

driver.get("https://www.saucedemo.com")
login_box = driver.find_element(By.CLASS_NAME, "login-box")

username = login_box.find_element(By.ID, "user-name")
username.send_keys("standard_user")

password = login_box.find_element(By.ID, "password")
password.send_keys("secret_sauce")
time.sleep(2)
login_button = login_box.find_element(By.ID, "login-button")
login_button.click()
# time.sleep(5)

# Task 2: Add Items to Cart from Inventory Page

sort_button = driver.find_element(By.TAG_NAME, "select")
sort_button.click()
# sort by xpath of prive low to high (3rd option)
driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/div/span/select/option[3]").click()

driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()

# time.sleep(5)

# Task 3: Add Items to Cart from Inventory Item Page
# move to product page n add item to cart

product = driver.find_element(By.LINK_TEXT, 'Sauce Labs Onesie')
product.click()

add_to_cart_btn = driver.find_element(By.ID,"add-to-cart")
add_to_cart_btn.click()

# time.sleep(5)


# Task 4: Remove Items from Cart
# remove items from cart
driver.find_element(By.CLASS_NAME,"shopping_cart_link").click() #move to cart
# time.sleep(5)
# remove item which costs between 8 and 10 $
cart_list = driver.find_element(By.CLASS_NAME,"cart_list")

cart_items = cart_list.find_elements(By.CLASS_NAME,"cart_item")

for item in cart_items:
    price_txt = item.find_element(By.CLASS_NAME,"inventory_item_price").text
    price = float(price_txt[1:])
    if price >= 8.00 and price <= 10.00:
        remove = item.find_element(By.CLASS_NAME,"cart_button")
        remove.click()
        # time.sleep(5)



# Task 5: Checkout Workflow
# check out
# time.sleep(5)
driver.find_element(By.CLASS_NAME,"checkout_button").click()

form = driver.find_element(By.TAG_NAME,"form")
first_name = form.find_element(By.ID,"first-name").send_keys("Kanhaiya")
last_name = form.find_element(By.ID,"last-name").send_keys("Sharma")
zip_code = form.find_element(By.ID,"postal-code").send_keys("110032")

continue_btn = form.find_element(By.ID,"continue")
continue_btn.click()

# time.sleep(5)
# printing total amount , 
checkout_container = driver.find_element(By.ID,"checkout_summary_container")

total_amt = checkout_container.find_element(By.CLASS_NAME,"summary_total_label").text
print(total_amt)
# time.sleep(5)
footer_container = driver.find_element(By.CLASS_NAME,"cart_footer")
finish_btn = footer_container.find_element(By.ID,"finish")
finish_btn.click()
# time.sleep(5)

driver.find_element(By.ID,"back-to-products").click()
# Task 6: Logout Functionality
# logout
time.sleep(5)
menu_btn = driver.find_element(By.ID,"react-burger-menu-btn")
menu_btn.click()
time.sleep(5)
# logout_btn = driver.find_element(By.ID,"logout_sidebar_link")
logout_btn = driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/nav/a[3]")

logout_btn.click()
time.sleep(5)

driver.close()
