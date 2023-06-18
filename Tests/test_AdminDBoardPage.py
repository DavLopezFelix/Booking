import pytest
from ..Pages.AdminDBoardPage import AdminDBoardPage
from ..Pages.AdminLoginPage import AdminPage
from ..Config.config import TestData
from ..Tests.test_base import BaseTest


class Test_AdminDBoardPanel(BaseTest):

    def test_new_message_inbox_admin(self):
        self.adminpage = AdminPage(self.driver)
        self.adminboard = self.adminpage.do_login_admin(TestData.ADMIN_USER, TestData.ADMIN_PASSWORD)
        self.adminboard.do_click_admin_inbox()
        messages = self.adminboard.get_quantity_NoRead_bookings()
        assert messages > 1

        