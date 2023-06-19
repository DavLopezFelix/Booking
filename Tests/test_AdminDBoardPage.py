import pytest
from ..Pages.AdminLoginPage import AdminPage
from ..Pages.AdminDBoardPage import AdminDBoardPage
from ..Config.config import TestData
from ..Tests.test_base import BaseTest

class Test_AdminDBoardPanel(BaseTest):

    def test_the_inbox_admin(self):
        self.adminpage = AdminPage(self.driver)
        self.adminboard = self.adminpage.do_login_admin(TestData.ADMIN_USER, TestData.ADMIN_PASSWORD)
        self.adminboard.do_click_admin_inbox()
        messages = self.adminboard.get_quantity_NoRead_bookings()
        assert messages > 1
    
    def test_the_new_message(self):
        self.adminboard = AdminDBoardPage(self.driver)
        self.adminboard.do_click_admin_inbox()
        self.adminboard.select_the_booking(TestData.BOOKING_SUBJECT, TestData.BOOKING_NAME)
        flag1 = self.adminboard.is_visisble_the_new_popup()
        assert flag1

        name = self.adminboard.get_from()
        phone = self.adminboard.get_phone()
        email = self.adminboard.get_email()
        subject = self.adminboard.get_subject()
        body = self.adminboard.get_body()
        assert TestData.BOOKING_NAME in name
        assert TestData.BOOKING_NUMBER in phone
        assert TestData.BOOKING_EMAIL in email
        assert TestData.BOOKING_SUBJECT in subject
        assert TestData.BOOKING_MESSAGE in body

        self.adminboard.close_popup()
        flag2 = self.adminboard.check_not_exist_popup()
        assert flag2

        value = self.adminboard.get_attr_read_message()
        assert TestData.ALREADY_READ_MESSAGE in value







        