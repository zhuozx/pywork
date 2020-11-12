from test_appium.page.basepage import BasePage
from test_appium.page.member_add import MemberAdd


class MemberAddSelect(BasePage):
    # 点击手动输入按钮
    def add_by_input(self):
        self.steps('../page/member_add_way.yaml', 'input')
        return MemberAdd(self.driver)
    # 获取添加结果提示
    def get_add_result(self):
        return self.steps('../page/member_add_way.yaml', 'getResult')
