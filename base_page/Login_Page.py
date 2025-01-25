from selenium.webdriver.common.by import By

class Login_Page:
    textbox_username_id = "user-name"
    text_password_id = "password"
    btn_login_id = "login-button"
    error_msg_xpath = "//*[@id='login_button_container']/div/form/div[3]/h3"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)
    
    def set_password(self, password):
        self.driver.find_element(By.ID, self.text_password_id).clear()
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.btn_login_id).click()
    
    def get_error_msg(self):
        return self.driver.find_element(By.XPATH, self.error_msg_xpath).text
    
    def get_current_url(self):
        return self.driver.current_url
