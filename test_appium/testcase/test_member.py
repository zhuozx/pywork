import allure
import pytest
from test_appium.page.app import App


class TestMember:
    # 启动app
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().main()

    def teardown_class(self):
        self.app.stop()

    @allure.story('添加成员')
    @pytest.mark.parametrize('name,phone', [('张三', '19911111111')])
    def test_add(self, name, phone):
        with allure.step('从首页进入通讯录页面，点击添加成员按钮,选择手动输入，输入成员信息并提交'):
            result = self.main.goto_contact().goto_add_member().add_by_input().add_member(
                name, phone).get_add_result()
        assert result == '添加成功'

    @allure.story('删除成员')
    @pytest.mark.parametrize('name', [('张三')])
    def test_del(self, name):
        with allure.step('从首页进入通讯录页面'):
            member_list = self.main.goto_contact()
            # 删除成员前，先获取到列表底部共xx人的文本，然后提取到总数
            total_str: str = member_list.get_member_number()
            total_num = int(total_str.split('，')[0][1:][:-1])
        with allure.step('进入搜索页面，点击搜索结果中的第一条数据，进入编辑页面进行删除操作'):
            del_action = member_list.goto_search().search(
                name).goto_person_info().goto_menu().goto_member_edit().del_member()
            # 删除成员后，再次获取到列表底部共xx人的文本，然后提取到总数
            del_after: str = del_action.go_back().get_member_number()
            del_after_num = int(del_after.split('，')[0][1:][:-1])
        # 删除前的总数等于删除后的总数加1，则成功
        assert total_num == del_after_num + 1
