import time

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.app import App


class TestMember:
    # 启动app
    def setup(self):
        self.app = App().start()

    def teardown(self):
        self.app.driver.quit()

    @pytest.mark.parametrize('name,phone', [('张三', '19911111111')])
    def test_add(self, name, phone):
        # 从首页进入通讯录页面，点击添加成员按钮
        member = self.app.main().goto_contact().goto_add_member()
        # 点击手动输入，进入添加成员页面，填写信息并提交
        member.add_by_input().add_member(name, phone)
        assert member.get_add_result() == '添加成功'

    @pytest.mark.parametrize('name', [('张三')])
    def test_del(self, name):
        # 从首页进入通讯录页面，点击搜索按钮
        member_search = self.app.main().goto_contact().goto_search()
        # 输入关键字，进行搜索
        member_search.search(name)
        # 获取删除成员前的查找到的成员个数
        del_before = member_search.get_number()
        # 点击第一个成员，进入编辑页面，点击删除按钮
        member_search.goto_person_info().goto_menu().goto_member_edit().del_member()
        # 获取删除成员后的查找到的成员个数
        del_after = member_search.get_number()
        assert del_before - 1 == del_after
