from base_page.Inventory_Page import Inventory_Page
from base_page.Product_Page import Product_Page
from utilities.read_properties import ReadConfig

class Test3:
    # item_text = 'Sauce Labs Onesie'
    item_text = ReadConfig.get_item_text()
    product_page = None

    def __init__(self, driver):
        self.driver = driver
        self.inventory = Inventory_Page(self.driver)
    
    def go_to_product_page(self):
        self.inventory.view_product(self.item_text)
        self.product_page = Product_Page(self.driver)
    
    def add_to_cart(self):
        # checking if the driver is is at product page
        if self.product_page is not None:
            prev_count = self.product_page.cart_count()
            self.product_page.add_to_cart()
            curr_count = self.product_page.cart_count()
            # validating if item is added to cart
            if curr_count == prev_count + 1:
                print("Item added to cart")
                print("Item count :", curr_count)
                assert True
            else:
                print("Item not added to cart")
                assert False
        else:
            print("Product page not loaded")
            assert False
