from test_appium.page.basepage import BasePage
from test_appium.page.member_edit import MemberEdit


class MemberMenu(BasePage):
    def goto_member_edit(self):
        self.steps('../page/member_menu.yaml','edit')
        return MemberEdit(self.driver)