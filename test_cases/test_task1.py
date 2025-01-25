import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_page.Login_Page import Login_Page
from utilities.read_properties import ReadConfig

class Test1:
    page_url = ReadConfig.get_page_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    invalid_username = ReadConfig.get_invalid_username()
    invalid_password = ReadConfig.get_invalid_password()
    error_msg = ReadConfig.get_error_msg()
    expected_url = ReadConfig.get_expected_url()

    def __init__(self,driver):
        self.driver = driver

    def test_valid_login(self):
        # self.driver = driver
        self.driver.get(self.page_url)
        login_page = Login_Page(self.driver)
        login_page.set_username(self.username)
        login_page.set_password(self.password)
        login_page.click_login()

        redirect_url = login_page.get_current_url()

        if( redirect_url == self.expected_url):
            print("valid case Test Passed")
            assert True
            # self.driver.close()
        else:
            print("invalid case Test Passed")
            assert False
            # self.driver.close()
    
    def test_invalid_login(self):
        # self.driver = driver
        self.driver.get(self.page_url)
        login_page = Login_Page(self.driver)
        login_page.set_username(self.invalid_username)
        login_page.set_password(self.invalid_password)
        login_page.click_login()

        error_msg = login_page.get_error_msg()

        if( error_msg == self.error_msg):
            print("invalid case Test Passed")
            assert True
            # self.driver.close()
        else:
            print("invalid case Test failed")
            assert False
            # self.driver.close()



