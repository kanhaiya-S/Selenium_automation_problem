from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Inventory_Page:
    expected_login_url = "https://www.saucedemo.com/"
    sort_button_tag = "select"
    price_low_high_xpath = "//*[@id='header_container']/div[2]/div/span/select/option[3]"
    cart_class_name = "shopping_cart_link"
    cart_count_class = "shopping_cart_badge"
    add_to_cart_btn_id = "add-to-cart"
    curr_cart_count = 0
    menu_btn_id = "react-burger-menu-btn"
    logout_btn_xpath = "/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/nav/a[3]"

    def __init__(self, driver):
        self.driver = driver
        self.curr_cart_count = self.cart_count()
    
    def sort_by_price_low_high(self):
        self.driver.find_element(By.TAG_NAME, self.sort_button_tag).click()
        self.driver.find_element(By.XPATH, self.price_low_high_xpath).click()
    
    def add_items_to_cart(self,item_ids):
        for item_id in item_ids:
            self.driver.find_element(By.ID, item_id).click()
            updated_cart_count = self.cart_count()
            if updated_cart_count != self.curr_cart_count + 1:
                print(f"Failed to add item {item_id} to cart")
            else:
                self.curr_cart_count = updated_cart_count
                print(f"Item {item_id} added to cart")
    
    def view_product(self, product_link_text):
        product_link = self.driver.find_element(By.LINK_TEXT, product_link_text)
        product_link.click()
    
    def view_cart(self):
        self.driver.find_element(By.CLASS_NAME,self.cart_class_name).click()
    
    def add_to_cart(self):
        add_to_cart_btn = self.driver.find_element(By.ID,self.add_to_cart_btn_id)
        add_to_cart_btn.click()
        updated_cart_count = self.cart_count()
        if updated_cart_count == self.curr_cart_count + 1:
            print("Item added to cart")
            self.curr_cart_count = updated_cart_count
        else:
            print("Item cannot be added to cart")
    
    def cart_count(self):
        try:
            return int(self.driver.find_element(By.CLASS_NAME, self.cart_count_class).text)
        except NoSuchElementException:
            return 0
    

    def click_menu(self):
        try:
            self.driver.find_element(By.ID,self.menu_btn_id).click()
        except NoSuchElementException:
            print("failed to find menu button")

    def click_logout(self):
        try:
            self.driver.find_element(By.XPATH,self.logout_btn_xpath).click()
            current_url = self.driver.current_url
            if current_url == self.expected_login_url:
                print("logout successful")
            else:
                print("failed to verify Logout")
        except NoSuchElementException:
            print("logout button not found")