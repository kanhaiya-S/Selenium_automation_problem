import configparser

config = configparser.RawConfigParser()

config.read(".\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def get_page_url():
        url = config.get('test1 info','page_url')
        return url
    
    @staticmethod
    def get_username():
        username = config.get('test1 info','username')
        return username
    
    @staticmethod
    def get_password():
        password = config.get('test1 info','password')
        return password
    
    
    @staticmethod
    def get_invalid_username():
        invalid_username = config.get('test1 info','invalid_username')
        return invalid_username
    
    @staticmethod
    def get_invalid_password():
        invalid_password = config.get('test1 info','invalid_password')
        return invalid_password
    
    @staticmethod
    def get_error_msg():
        error_msg = config.get('test1 info','error_msg')
        return error_msg
    
    @staticmethod
    def get_expected_url():
        expected_url = config.get('test1 info','expected_url')
        return expected_url
    
    @staticmethod
    def get_item_ids():
        ids = config.get('test2 info','items_ids').split(',')
        return ids
    
    @staticmethod
    def get_item_text():
        text = config.get('test3 info','item_text')
        return text
    
    @staticmethod
    def get_min_price():
        price = config.get('test4 info','min_price')
        return int(price)
    
    @staticmethod
    def get_max_price():
        price = config.get('test4 info','max_price')
        return int(price)
    
    @staticmethod
    def get_expected_cart_count():
        count = config.get('test4 info','expected_cart_count')
        return int(count)
    
    @staticmethod
    def get_cart_link_classname():
        classname = config.get('test4 info','cart_link_classname')
        return classname
    
    @staticmethod
    def get_exp_cart_url():
        url = config.get('test4 info','exp_cart_url')
        return url
    
    @staticmethod
    def get_checkout_btn_id():
        id = config.get('test5 info','checkout_btn_id')
        return id
    
    @staticmethod
    def get_first_name():
        first_name = config.get('test5 info','first_name')
        return first_name
    
    @staticmethod
    def get_zip_code():
        zipcode = config.get('test5 info','zip_code')
        return zipcode
    
    @staticmethod
    def get_expected_checkout_two_url():
        url = config.get('test5 info','expected_checkout_two_url')
        return url
    
    @staticmethod
    def get_last_name():
        lastname = config.get('test5 info','last_name')
        return lastname
    
    @staticmethod
    def get_expected_checkout_msg():
        msg = config.get('test5 info','expected_checkout_msg')
        return msg