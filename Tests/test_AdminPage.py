import pytest
from ..Pages.AdminPage import AdminPage
from ..Config.config import TestData
from ..Tests.test_base import BaseTest
from time import sleep


class Test_AdminPanel(BaseTest):

    def test_admingpage_header(self):
        self.adminpage = AdminPage(self.driver)
        text = self.adminpage.get_admin_login_header()
        assert text == TestData.ADMIN_LOGIN_HEADER

    def test_login_admin(self):
        self.adminpage = AdminPage(self.driver)
        self.adminpage.do_login_admin(TestData.ADMIN_USER, TestData.ADMIN_PASSWORD)

        sleep(2)

        login_header = self.adminpage.get_header_admin_panel()
        assert TestData.ADMIN_PANEL_HEADER == login_header
        