from test_appium.page.basepage import BasePage
from test_appium.page.member_add_way import MemberAddSelect
from test_appium.page.member_search import MemberSearch


class MemberList(BasePage):
    def goto_add_member(self):
        self.steps('../page/member_list.yaml','addMemberBtn')
        return MemberAddSelect(self.driver)

    def goto_search(self):
        self.steps('../page/member_list.yaml','search')
        return MemberSearch(self.driver)

