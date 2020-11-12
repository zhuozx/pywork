from test_appium.page.basepage import BasePage
from test_appium.page.member_menu import MemberMenu


class MemberInfo(BasePage):
    def goto_menu(self):
        self.steps('../page/member_info.yaml','menu')
        return MemberMenu(self.driver)