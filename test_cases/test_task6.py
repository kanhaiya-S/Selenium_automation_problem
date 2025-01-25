from selenium.webdriver.common.by import By
from base_page.Inventory_Page import Inventory_Page
from base_page.Product_Page import Product_Page
from base_page.Cart_Page import Cart_Page
from base_page.CheckOut_Page import CheckOut_Page
from selenium.common.exceptions import NoSuchElementException
from utilities.read_properties import ReadConfig

import time

class Test6:
    inventory_page = None
    def __init__(self,driver):
        self.driver = driver
        self.inventory_page = Inventory_Page(self.driver)
        
    def test_logout(self):
        try:
            # time.sleep(3)
            self.inventory_page.click_menu()
            time.sleep(3)
            self.inventory_page.click_logout()
            # time.sleep(3)
        except NoSuchElementException:
            print("Failed Testing Logout")