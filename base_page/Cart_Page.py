from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Cart_Page:
    cart_list_class = "cart_list"
    cart_item_class = "cart_item"
    inventory_item_price_class = "inventory_item_price"
    checkout_button_class = "checkout_button"
    cart_class_name = "shopping_cart_link"
    cart_link = "shopping_cart_link"
    cart_count_class = "shopping_cart_badge"

    def __init__(self, driver):
        self.driver = driver
    
    # a method to proceed to checkout
    def move_to_checkout(self):
        self.driver.find_element(By.CLASS_NAME, self.checkout_button_class).click()
    
    # to get current url
    def get_current_url(self):
        return self.driver.current_url
    
    # to fetch items in cart
    def get_cart_items(self):
        return self.driver.find_elements(By.CLASS_NAME, self.cart_item_class)
    
    # to get price
    def get_cart_item_price(self, item):
        price_txt = item.find_element(By.CLASS_NAME, self.inventory_item_price_class).text
        return float(price_txt[1:])
    
    # get count of items in cart
    def cart_count(self):
        try:
            return int(self.driver.find_element(By.CLASS_NAME, self.cart_count_class).text)
        except NoSuchElementException:
            return 0

    # remove item from cart 
    def remove_item(self, item):
        item.find_element(By.CLASS_NAME, "cart_button").click()
    
    # remove items from cart based on price range
    def filter_cart_items_by_range(self,minvalue, maxvalue):
        items = self.get_cart_items()
        for item in items:
            price = self.get_cart_item_price(item)
            if price >= minvalue and price <= maxvalue:
                self.remove_item(item)
        curr_cart_count = self.cart_count()
        print(f"Item Count in cart after filtering: {curr_cart_count}")
