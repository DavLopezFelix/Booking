import random

class TestData():
    CHROME_EXECUTABLE_PATH = "C://SeleniumDrivers//chromedriver_win32//chromedriver.exe"
    FIREFOX_EXECUTABLE_PATH = "C://SeleniumDrivers//geckodriver-v0.33.0-win32"

    BASE_URL = 'https://automationintesting.online/'

    BOOKING_TITLE = 'Restful-booker-platform demo'
    BOOKING_NAME = 'David'
    BOOKING_EMAIL = 'david@ho.com'
    BOOKING_NUMBER = '656656565464656'
    BOOKING_SUBJECT = f'Test subject - {random.randint(0,500)}'
    BOOKING_MESSAGE = 'These is the body'*10

    ADMIN_LOGIN_HEADER = 'Log into your account'
    ADMIN_USER = 'admin'
    ADMIN_PASSWORD = 'password'
    ADMIN_PANEL_HEADER = 'Logout'
