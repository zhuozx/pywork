from test_appium.page.basepage import BasePage
from test_appium.page.member_invite import MemberInvite
from test_appium.page.member_search import MemberSearch


# 通讯录列表页面
class MemberList(BasePage):
    # 获取成员列表个数
    def get_member_number(self):
        return self.steps('../data/member_list.yaml', 'getMemberNum')

    # 点击底部的添加成员按钮
    def goto_add_member(self):
        self.steps('../data/member_list.yaml', 'addMemberBtn')
        return MemberInvite(self.driver)

    # 点击搜索按钮进入搜索页面
    def goto_search(self):
        self.steps('../data/member_list.yaml', 'search')
        return MemberSearch(self.driver)
