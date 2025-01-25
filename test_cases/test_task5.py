from selenium.webdriver.common.by import By
from base_page.Inventory_Page import Inventory_Page
from base_page.Product_Page import Product_Page
from base_page.Cart_Page import Cart_Page
from base_page.CheckOut_Page import CheckOut_Page
from selenium.common.exceptions import NoSuchElementException
from utilities.read_properties import ReadConfig

import time

class Test5:
    # checkout_btn_id = "checkout"
    # first_name = "kanhaiya"
    # last_name = "sharma"
    # zip_code = 111111
    # expected_checkout_two_url = "https://www.saucedemo.com/checkout-step-two.html"
    # expected_checkout_msg = "Thank you for your order!"
    checkout_btn_id = ReadConfig.get_checkout_btn_id()
    first_name = ReadConfig.get_first_name()
    last_name = ReadConfig.get_last_name()
    zip_code = ReadConfig.get_zip_code()
    expected_checkout_two_url = ReadConfig.get_expected_checkout_two_url()
    expected_checkout_msg = ReadConfig.get_expected_checkout_msg()

    checkout_page = None
    def __init__(self,driver):
        self.driver = driver
        try:
            self.driver.find_element(By.ID,self.checkout_btn_id).click()
            self.checkout_page = CheckOut_Page(self.driver)
        except NoSuchElementException:
            print(f"Couldn't move to checkout")

    def test_fill_form(self):
        self.checkout_page.set_first_name(self.first_name)
        self.checkout_page.set_last_name(self.last_name)
        self.checkout_page.set_zip_code(self.zip_code)

        self.checkout_page.click_continue()
        
        if self.driver.current_url == self.expected_checkout_two_url:
            print("form validation complete")
        else:
            print("form validation failed")
    
    def test_print_amount(self):
        total_amt = self.checkout_page.get_total_price()
        print("Total amount: ",total_amt)
    
    def test_checkout(self):
        try:
            self.checkout_page.click_finish()
            text_msg = self.checkout_page.get_complete_msg()

            if(text_msg == self.expected_checkout_msg ):
                print(" final checkout message Verified")
                self.checkout_page.go_home_page()
            else:
                print(" failed to verity final checkout message")
        except NoSuchElementException:
            print("Failed to checkout")
