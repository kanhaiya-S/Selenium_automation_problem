# Task 2: Add Items to Cart from Inventory Page
from base_page.Inventory_Page import Inventory_Page
from utilities.read_properties import ReadConfig

class Test2:
    # items_ids = ["add-to-cart-sauce-labs-backpack", "add-to-cart-sauce-labs-bike-light"]
    # hardcoded ids moved to config.ini file
    items_ids = ReadConfig.get_item_ids()

    def __init__(self,driver):
        self.driver = driver
        self.inventory = Inventory_Page(self.driver)
    
    def add_items(self):
        self.inventory.add_items_to_cart(self.items_ids)
    
    def filter_items(self):
        self.inventory.sort_by_price_low_high()

