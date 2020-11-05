from test_selenium.page.main import Main


class TestMember:
    def setup(self):
        self.main = Main()
        # 浏览器复用-保存cookies
        self.main.save_cookies()
        # 使用cookies登录
        # self.main.login_with_cookies()

    def teardown(self):
        self.main.driver.quit()

    def test_add_member(self):
        add_member = self.main.goto_add_member()
        member_list = add_member.add_member()
        assert add_member.name in member_list.get_member_name()

