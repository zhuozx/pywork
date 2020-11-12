from test_appium.page.basepage import BasePage
from test_appium.page.member_info import MemberInfo


class MemberSearch(BasePage):
    def search(self, name):
        self.params['key'] = name
        self.steps('../page/member_search.yaml', 'key')
        return self

    def get_number(self):
        return self.steps('../page/member_search.yaml', 'result')

    def goto_person_info(self):
        self.steps('../page/member_search.yaml', 'click')
        return MemberInfo(self.driver)
