from test_appium.page.basepage import BasePage


class MemberEdit(BasePage):
    def del_member(self):
        self.steps('../page/member_edit.yaml','del')
