from selenium.webdriver.common.by import By
from base_page.Inventory_Page import Inventory_Page
from base_page.Product_Page import Product_Page
from base_page.Cart_Page import Cart_Page
from utilities.read_properties import ReadConfig

import time
class Test4:
    # min_price = 8
    # max_price = 10
    min_price = ReadConfig.get_min_price() # 8
    max_price = ReadConfig.get_max_price() # 10
    expected_cart_count = ReadConfig.get_expected_cart_count()
    cart_link_classname = ReadConfig.get_cart_link_classname()
    exp_cart_url = ReadConfig.get_exp_cart_url()
    # exp_cart_url = "https://www.saucedemo.com/cart.html"
    def __init__(self, driver):
        self.driver = driver
        self.cart_page= Cart_Page(self.driver)
    
    def view_cart(self):
        self.driver.find_element(By.CLASS_NAME, self.cart_link_classname).click()

    def filter_by_items(self):
        self.view_cart()
        # time.sleep(3)
        self.cart_page.filter_cart_items_by_range(self.min_price,self.max_price)
        curr_cart_count = self.cart_page.cart_count()

        if curr_cart_count != self.expected_cart_count:
            print(f"Failed to validate cart count")
            assert False
        else:
            print(f"cart count Validated , count : {curr_cart_count}")
        

