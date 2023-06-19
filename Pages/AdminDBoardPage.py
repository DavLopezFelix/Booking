from selenium.webdriver.common.by import By
from .BasePage import BasePage
from ..Config.config import TestData
from time import sleep


class AdminDBoardPage(BasePage):
    
    """By locators"""
    ADMIN_INBOX = (By.XPATH, '//i[@class="fa fa-inbox"]')
    NOREAD_BOOKINGS = (By.CSS_SELECTOR, '.row.detail.read-false')
    NAME_NOREAD_BOOKINGS = (By.XPATH, '//div[@class="row detail read-false"]/div[1]')
    SUBJECT_NOREAD_BOOKINGS = (By.XPATH, '//div[@class="row detail read-false"]/div[2]')
    POPUP_MESSAGE = (By.XPATH, '//div[@data-testid="message"]')
    FROM = (By.XPATH, '//div[@data-testid="message"]/div[1]/div[1]')
    PHONE = (By.XPATH, '//div[@data-testid="message"]/div[1]/div[2]')
    EMAIL = (By.XPATH, '//div[@data-testid="message"]/div[2]')
    SUBJECT = (By.XPATH, '//div[@data-testid="message"]/div[3]/div/p')
    BODY = (By.XPATH, '//div[@data-testid="message"]/div[4]')

    CLOSE_BUTTON = (By.XPATH, '//div[@data-testid="message"]/div[5]/div/button')


    """"Constructor of the pages class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(f'{TestData.BASE_URL}/#/admin')


    """Booking Actions for Booking Page"""   
    def do_click_admin_inbox(self):
        self.do_click(self.ADMIN_INBOX)
    
    def get_quantity_NoRead_bookings(self):
        return self.get_quantity_elements(self.NOREAD_BOOKINGS)
    
    def select_the_booking(self, subject, name):
        elements = self.get_elements(self.SUBJECT_NOREAD_BOOKINGS)
        for i, element_subject in enumerate(elements):
            if subject in element_subject.text:
                SELECTED_NAME_BOOKING = (By.XPATH, \
                                        f'//div[@class="row detail read-false"][{i+1}]/div[1]')
                element_name = self.get_elment_text(SELECTED_NAME_BOOKING)

                if name in element_name:
                    print("I found it!")
                    SELECTED_SUBJECT_BOOKING = (By.XPATH, \
                                        f'//div[@class="row detail read-false"][{i+1}]/div[2]')
                    self.do_click(SELECTED_SUBJECT_BOOKING)
                    sleep(1)

    def is_visisble_the_new_popup(self):
        return self.is_visible(self.POPUP_MESSAGE)
    
    def get_from(self):
        element = self.get_innerHTML_text(self.FROM)
        print(element)
        return element
    
    def get_phone(self):
        element = self.get_innerHTML_text(self.PHONE)
        return element
    
    def get_email(self):
        element = self.get_innerHTML_text(self.EMAIL)
        return element
    
    def get_subject(self):
        element = self.get_innerHTML_text(self.SUBJECT)
        return element
    
    def get_body(self):
        element = self.get_innerHTML_text(self.BODY)
        return element

    def close_popup(self):
        self.do_click(self.CLOSE_BUTTON)
    



        