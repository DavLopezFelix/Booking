from selenium.webdriver.common.by import By
from .BasePage import BasePage
from ..Config.config import TestData


class BookingPage(BasePage):
    
    """By locators"""
    MAIN_PICTURE = (By.XPATH, "//div[@class='row']/div[1]/img")
    NAME = (By.ID, 'name')
    EMAIL = (By.ID, 'email')
    PHONE = (By.ID, 'phone')
    SUBJECT = (By.ID, 'subject')
    MESSAGE = (By.ID, 'description')
    SUBMIT = (By.ID, 'submitContact')

    SUBMITTED_NAME = (By.XPATH, '//div[@class="row contact"]//div[2]//h2')
    SUBMITTED_SUBJECT = (By.XPATH, '//div[@class="row contact"]//div[2]//p[2]')

    """"Constructor of the pages class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Booking Actions for Booking Page"""

    def get_booking_page_title(self, title):
        return self.get_title(title)
    
    def is_main_logo_visible(self):
        return self.is_visible(self.MAIN_PICTURE)
    
    def create_booking(self, name, email, phone, subject, message):
        self.do_send_keys(self.NAME, name)
        self.do_send_keys(self.EMAIL, email)
        self.do_send_keys(self.PHONE, phone)
        self.do_send_keys(self.SUBJECT, subject)
        self.do_send_keys(self.MESSAGE, message)
        self.do_click(self.SUBMIT)
       
    def get_name_sumitted_text(self):
        element = self.get_elment_text(self.SUBMITTED_NAME)
        return element
    
    def get_subject_sumitted_text(self):
        element = self.get_elment_text(self.SUBMITTED_SUBJECT)
        return element