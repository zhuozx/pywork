from test_appium.page.basepage import BasePage


class MemberAdd(BasePage):
    # 添加成员页面
    def add_member(self, name, phone):
        self.params['name'] = name
        self.params['phone'] = phone
        #打开yaml文件，并对add对应的value进行定位操作
        self.steps('../page/member_add.yaml','add')
