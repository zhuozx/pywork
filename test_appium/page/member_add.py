from test_appium.page.basepage import BasePage


# 添加成员页面
class MemberAdd(BasePage):
    def add_member(self, name, phone):
        # 重写基类中的_params，用于后续steps中替换参数化变量
        self._params['name'] = name
        self._params['phone'] = phone
        # 打开yaml文件，并对key为add对应的value进行定位操作
        self.steps('../data/member_add.yaml', 'add')
        from test_appium.page.member_invite import MemberInvite
        return MemberInvite(self.driver)
