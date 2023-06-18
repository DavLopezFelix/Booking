from selenium.webdriver.common.by import By
from .BasePage import BasePage
from ..Config.config import TestData


class AdminDBoardPage(BasePage):
    
    """By locators"""
    ADMIN_INBOX = (By.XPATH, '//i[@class="fa fa-inbox"]')
    NOREAD_BOOKINGS = (By.CSS_SELECTOR, '.row.detail.read-false')


    """"Constructor of the pages class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(f'{TestData.BASE_URL}/#/admin')


    """Booking Actions for Booking Page"""   
    def do_click_admin_inbox(self):
        self.do_click(self.ADMIN_INBOX)
    
    def get_quantity_NoRead_bookings(self):
        return self.get_quantity_elements(self.NOREAD_BOOKINGS)
