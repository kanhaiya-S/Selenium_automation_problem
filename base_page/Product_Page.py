from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Product_Page:
    add_to_cart_btn_id = "add-to-cart"
    cart_class_name = "shopping_cart_link"
    cart_count_class = "shopping_cart_badge"

    def __init__(self, driver):
        self.driver = driver
        self.curr_cart_count = self.cart_count()
    
    def view_product(self, product_link_text):
        self.driver.find_element(By.LINK_TEXT, product_link_text).click()
    
    def add_to_cart(self):
        add_to_cart_btn = self.driver.find_element(By.ID,self.add_to_cart_btn_id)
        add_to_cart_btn.click()
        updated_cart_count = self.cart_count()
        if updated_cart_count == self.curr_cart_count + 1:
            print("Item added to cart")
            self.curr_cart_count = updated_cart_count
        else:
            print("Item cannot be added to cart")
    
    def remove_from_cart(self):
        add_to_cart_btn = self.driver.find_element(By.ID,self.add_to_cart_btn_id)
        add_to_cart_btn.click()
        updated_cart_count = self.cart_count()
        if updated_cart_count == self.curr_cart_count - 1:
            print("Item removed from cart")
            self.curr_cart_count = updated_cart_count
        else:
            print("Item cannot be removed from cart")

    def view_cart(self):
        self.driver.find_element(By.CLASS_NAME,self.cart_class_name).click()
    
    def cart_count(self):
        try:
            return int(self.driver.find_element(By.CLASS_NAME, self.cart_count_class).text)
        except NoSuchElementException:
            return 0