from test_appium.page.basepage import BasePage
from test_appium.page.member_edit import MemberEdit


# 个人信息菜单项
class MemberMenu(BasePage):
    # 点击编辑按钮进入成员编辑页面
    def goto_member_edit(self):
        self.steps('../data/member_menu.yaml', 'edit')
        return MemberEdit(self.driver)
