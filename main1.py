from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_cases.test_task1 import Test1
from test_cases.test_task2 import Test2
from test_cases.test_task3 import Test3
from test_cases.test_task4 import Test4
from test_cases.test_task5 import Test5
from test_cases.test_task6 import Test6
import time

driver = webdriver.Chrome()

# Task 1: Login Validation
test1 = Test1(driver)
test1.test_invalid_login()  #test invalid login
test1.test_valid_login()  #test valid login

# Task 2: Add Items to Cart from Inventory Page
test2 = Test2(driver)
test2.filter_items()
test2.add_items()

# # Task 3: Add Items to Cart from Inventory Item Page
test3 = Test3(driver)
test3.go_to_product_page()
test3.add_to_cart()
time.sleep(3)


# Task 4: Remove Items from Cart

test4 = Test4(driver)
# time.sleep(3)
test4.filter_by_items()
time.sleep(3)

test5 = Test5(driver)
test5.test_fill_form()
# time.sleep(3)
test5.test_print_amount()
time.sleep(3)
test5.test_checkout()
# time.sleep(3)


test6 = Test6(driver)
test6.test_logout()

driver.quit()