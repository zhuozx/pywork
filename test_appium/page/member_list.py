from test_appium.page.basepage import BasePage
from test_appium.page.member_add_select import MemberAddSelect


class MemberList(BasePage):
    def goto_add_member(self):
        self.steps('../page/member_list.yaml')
        return MemberAddSelect(self.driver)

    def goto_search(self):
        pass

