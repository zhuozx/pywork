from test_appium.page.basepage import BasePage
from test_appium.page.member_list import MemberList


class MemberAdd(BasePage):
    def add_member(self, name, phone):
        self.params['name'] = name
        self.params['phone'] = phone
        print(self.params)
        self.steps('../page/member_add.yaml')
        return MemberList(self.driver)
