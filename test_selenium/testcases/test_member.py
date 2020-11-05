import allure
from test_selenium.page.main import Main


@allure.feature('通讯录-成员管理')
class TestMember:
    def setup_class(self):
        self.main = Main()
        # 浏览器复用-保存cookies
        # self.main.save_cookies()
        # 使用cookies登录
        self.main.login_with_cookies()

    def teardown_class(self):
        self.main.driver.quit()

    @allure.story('添加成员')
    def test_add_member(self):
        with allure.step('进入首页点击底部的【添加成员按钮】'):
            add_member = self.main.goto_add_member()
        with allure.step('填写信息并提交后自动返回列表'):
            member_list = add_member.add_member()
        # 断言，刚添加的成员姓名是否在列表中
        assert add_member.name in member_list.get_member_name()

    @allure.story('删除成员')
    def test_del_member(self):
        self.main.goto_member_list().del_member()
