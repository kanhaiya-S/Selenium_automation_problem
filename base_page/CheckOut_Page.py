from selenium.webdriver.common.by import By

class CheckOut_Page:
    first_name_id = "first-name"
    last_name_id = "last-name"
    zip_code_id = "postal-code"
    continue_button_id = "continue"
    finish_btn_id = "finish"
    total_price_class = "summary_total_label"
    msg_class = "complete-header"
    go_home_btn_id = "back-to-products"

    def __init__(self, driver):
        self.driver = driver

    def set_first_name(self, first_name):
        self.driver.find_element(By.ID, self.first_name_id).clear()
        self.driver.find_element(By.ID, self.first_name_id).send_keys(first_name)
    
    def set_last_name(self, last_name):
        self.driver.find_element(By.ID, self.last_name_id).clear()
        self.driver.find_element(By.ID, self.last_name_id).send_keys(last_name)
    
    def set_zip_code(self, zip_code):
        self.driver.find_element(By.ID, self.zip_code_id).clear()
        self.driver.find_element(By.ID, self.zip_code_id).send_keys(zip_code)
    
    def click_continue(self):
        self.driver.find_element(By.ID, self.continue_button_id).click()

    def get_total_price(self):
        return float(self.driver.find_element(By.CLASS_NAME, self.total_price_class).text[8:])
    
    def click_finish(self):
        self.driver.find_element(By.ID, self.finish_btn_id).click()

    def get_complete_msg(self):
        return self.driver.find_element(By.CLASS_NAME,self.msg_class).text

    def go_home_page(self):
        self.driver.find_element(By.ID, self.go_home_btn_id).click()

    def get_current_url(self):
        return self.driver.current_url
    