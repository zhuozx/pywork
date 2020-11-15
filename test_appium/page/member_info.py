from test_appium.page.basepage import BasePage
from test_appium.page.member_menu import MemberMenu


# 个人信息页面
class MemberInfo(BasePage):
    # 点击右上角按钮进入菜单项
    def goto_menu(self):
        self.steps('../data/member_info.yaml', 'menu')
        return MemberMenu(self.driver)
