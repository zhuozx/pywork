from test_appium.page.basepage import BasePage


# 搜索页面
class MemberSearch(BasePage):
    # 搜索功能
    def search(self, name):
        # 重写基类的_params，后续用于替换参数化内容
        self._params['key'] = name
        self.steps('../data/member_search.yaml', 'key')
        return self

    # 返回上一页
    def go_back(self):
        self.steps('../data/member_search.yaml', 'back')
        from test_appium.page.member_list import MemberList
        return MemberList(self.driver)

    # 进入个人信息页面
    def goto_person_info(self):
        self.steps('../data/member_search.yaml', 'click')
        from test_appium.page.member_info import MemberInfo
        return MemberInfo(self.driver)
