from test_appium.page.basepage import BasePage
from test_appium.page.member_add import MemberAdd


class MemberAddSelect(BasePage):
    def add_by_input(self):
        self.steps('../page/member_add_select.yaml')
        return MemberAdd(self.driver)
