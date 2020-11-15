from test_appium.page.basepage import BasePage


# 添加成员方式页面
class MemberInvite(BasePage):
    # 点击手动输入按钮
    def add_by_input(self):
        self.steps('../data/member_add_way.yaml', 'input')
        from test_appium.page.member_add import MemberAdd
        return MemberAdd(self.driver)

    # 获取添加结果提示
    def get_add_result(self):
        return self.steps('../data/member_add_way.yaml', 'getResult')
