import time

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.app import App


class TestMember:
    def setup(self):
        self.app = App().start()

    def teardown(self):
        self.app.driver.quit()

    @pytest.mark.parametrize('name,phone', [('张三', '19911111111')])
    def test_add(self, name, phone):
        self.app.main().goto_contact().goto_add_member().add_by_input().add_member(name,phone)
