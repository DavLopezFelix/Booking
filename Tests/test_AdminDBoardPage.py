import pytest
from ..Pages.AdminLoginPage import AdminPage
from ..Pages.AdminDBoardPage import AdminDBoardPage
from ..Config.config import TestData
from ..Tests.test_base import BaseTest

class Test_AdminDBoardPanel(BaseTest):

    def test_click_the_inbox_admin(self):
        self.adminpage = AdminPage(self.driver)
        self.adminboard = self.adminpage.do_login_admin(TestData.ADMIN_USER, TestData.ADMIN_PASSWORD)
        self.adminboard.do_click_admin_inbox()
        messages = self.adminboard.get_quantity_NoRead_bookings()
        assert messages > 1
    
    def test_booking_details(self):
        #self.adminpage = AdminPage(self.driver)
        #self.adminboard = self.adminpage.do_login_admin(TestData.ADMIN_USER, TestData.ADMIN_PASSWORD)
        self.adminboard = AdminDBoardPage(self.driver)
        self.adminboard.do_click_admin_inbox()
        self.adminboard.select_the_booking(TestData.BOOKING_SUBJECT, TestData.BOOKING_NAME)
        flag = self.adminboard.is_visisble_the_new_popup()
        name = self.adminboard.get_from()
        phone = self.adminboard.get_phone()
        email = self.adminboard.get_email()
        subject = self.adminboard.get_subject()
        body = self.adminboard.get_body()
        assert flag
        assert TestData.BOOKING_NAME in name
        assert TestData.BOOKING_NUMBER in phone
        assert TestData.BOOKING_EMAIL in email
        assert TestData.BOOKING_SUBJECT in subject
        assert TestData.BOOKING_MESSAGE in body


        