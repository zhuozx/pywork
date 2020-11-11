from test_appium.page.basepage import BasePage
from test_appium.page.member_list import MemberList


class Main(BasePage):
    def goto_contact(self):
        self.steps('../page/main.yaml')
        return MemberList(self.driver)
    