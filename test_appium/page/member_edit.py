from test_appium.page.basepage import BasePage


# 编辑成员页面
class MemberEdit(BasePage):
    # 点击删除按钮，删除成员
    def del_member(self):
        self.steps('../data/member_edit.yaml', 'del')
        from test_appium.page.member_search import MemberSearch
        return MemberSearch(self.driver)
