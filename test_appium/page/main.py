from test_appium.page.basepage import BasePage
from test_appium.page.member_list import MemberList


class Main(BasePage):
    # 跳转到通讯录页面
    def goto_contact(self):
        self.steps('../page/main.yaml','contact')
        return MemberList(self.driver)
