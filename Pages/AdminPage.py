from selenium.webdriver.common.by import By
from .BasePage import BasePage
from ..Config.config import TestData


class AdminPage(BasePage):
    
    """By locators"""
    ADMIN_TITILE = (By.CSS_SELECTOR, 'h2[data-testid = "login-header"]')
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'doLogin')

    ADMIN_PANEL = (By.XPATH, '//div[@class="navbar-collapse collapse w-100 order-3 dual-collapse2"]/ul/li[3]')

    """"Constructor of the pages class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(f'{TestData.BASE_URL}/#/admin')


    """Booking Actions for Booking Page"""   
    def get_admin_login_header(self):
        element = self.get_elment_text(self.ADMIN_TITILE)
        return element
    
    def do_login_admin(self, username, password):
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)

    def get_header_admin_panel(self):
        element = self.get_elment_text(self.ADMIN_PANEL)
        return element