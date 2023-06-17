import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from ..Config.config import TestData

@pytest.fixture(params=['chrome'], scope = 'class')
def init_driver(request):

    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        serv_obj = Service(TestData.CHROME_EXECUTABLE_PATH)
        web_driver = webdriver.Chrome(service = serv_obj, options = options)
    if request.param == 'firefox':
        serv_obj = Service(TestData.FIREFOX_EXECUTABLE_PATH)
        web_driver = webdriver.Firefox(service = serv_obj)
    request.cls.driver =  web_driver
    yield
    web_driver.close()