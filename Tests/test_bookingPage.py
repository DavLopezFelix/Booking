import pytest
from ..Pages.BookingPage import BookingPage
from ..Config.config import TestData
from ..Tests.test_base import BaseTest
from time import sleep


class Test_BookingPage(BaseTest):

    def test_bookingpage_title(self):
        self.bookingpage = BookingPage(self.driver)
        title = self.bookingpage.get_booking_page_title(TestData.BOOKING_TITLE)
        assert title == TestData.BOOKING_TITLE

    def test_main_picture_is_visible(self):
        self.bookingpage = BookingPage(self.driver)
        flag = self.bookingpage.is_main_logo_visible()
        assert flag

    def test_create_booking(self):
        self.bookingpage = BookingPage(self.driver)
        self.bookingpage.create_booking(TestData.BOOKING_NAME, TestData.BOOKING_EMAIL,\
                                        TestData.BOOKING_NUMBER, TestData.BOOKING_SUBJECT,\
                                        TestData.BOOKING_MESSAGE)
        submitted_name = self.bookingpage.get_name_sumitted_text()
        submitted_message = self.bookingpage.get_subject_sumitted_text()

        assert TestData.BOOKING_NAME in submitted_name and \
                TestData.BOOKING_SUBJECT in submitted_message
        