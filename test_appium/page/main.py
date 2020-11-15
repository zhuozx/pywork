from test_appium.page.basepage import BasePage
from test_appium.page.member_list import MemberList


class Main(BasePage):
    # 从首页进入通讯录页面
    def goto_contact(self):
        self.steps('../data/main.yaml', 'contact')
        return MemberList(self.driver)
