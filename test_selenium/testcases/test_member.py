import allure
from test_selenium.page.main import Main


@allure.feature('通讯录-成员管理')
class TestMember:
    def setup(self):
        self.main = Main()
        # 浏览器复用-保存cookies
        self.main.save_cookies()
        # 使用cookies登录
        # self.main.login_with_cookies()

    def teardown(self):
        self.main.driver.quit()

    @allure.story('添加成员')
    def test_add_member(self):
        with allure.step('进入首页点击底部的【添加成员按钮】,填写信息并提交'):
            add_member = self.main.goto_add_member()
            add_member.add_member()
            assert add_member.get_member_name(add_member.name)

    @allure.story('删除成员')
    def test_del_member(self):
        assert self.main.goto_member_list().del_member()
