import allure
import pytest
import yaml
from jsonpath import jsonpath
from test_requests.tag import Tag

with open('tag.yaml') as f:
    data = yaml.safe_load(f)


class TestTag:
    def setup_class(self):
        self.tag = Tag()
        self.tag.get_token()
        # 清理数据
        r = self.tag.list()
        if r.json()['tag_group']:
            group_ids = jsonpath(r.json(), '$..group_id')
            self.tag.delete(group_ids)

    @allure.story('测试添加正常标签')
    @pytest.mark.parametrize('group_name,tag_names', data['normal'])
    def test_add(self, group_name, tag_names):
        # 添加标签
        r = self.tag.add(group_name, tag_names)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

        # 获取标签列表
        r = self.tag.list()
        # 使用jsonpath取到所有name字段值，如果测试数据tag_names是其子集，则表示添加成功
        assert set(tag_names) <= set(jsonpath(r.json(), '$..name'))

    @allure.story('测试添加重复标签')
    @pytest.mark.parametrize('group_name,tag_names', data['normal'])
    def test_add_fail_exist(self, group_name, tag_names):
        # 添加标签
        r = self.tag.add(group_name, tag_names)
        r = self.tag.add(group_name, tag_names)
        assert r.status_code == 200
        assert r.json()['errcode'] == 40071

    @allure.story('测试添加超长标签')
    @pytest.mark.parametrize('group_name,tag_names', data['fail'])
    def test_add_fail_overlong(self, group_name, tag_names):
        # 添加标签
        r = self.tag.add(group_name, tag_names)
        assert r.status_code == 200
        assert r.json()['errcode'] == 40058

    @allure.story('测试查询全部标签')
    def test_list(self):
        r = self.tag.list()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    @allure.story('测试用存在的tag_id查询标签')
    def test_list_by_tag(self):
        # 获取所有id节点
        r = self.tag.list()
        if r.json()['tag_group']:
            tag_id = jsonpath(r.json(), '$..id')
            r = self.tag.list(tag_id)
            assert r.status_code == 200
            assert r.json()['errcode'] == 0
            # 使用jsonpath取到所有id值，如果获取的结果是测试数据tag_id的子集，则表示成功查询到了标签
            assert not set(tag_id) - set(jsonpath(r.json(), '$..id'))
        else:
            print('没有可查询的标签')

    @allure.story('测试用不存在的tag_id查询标签')
    def test_list_fail(self):
        r = self.tag.list(['xxxxxxxxxx'])
        assert r.status_code == 200
        assert r.json()['errcode'] == 40068

    @allure.story('测试删除存在的标签')
    def test_del(self):
        # 获取标签列表
        r = self.tag.list()
        if r.json()['tag_group']:
            group_ids = jsonpath(r.json(), '$..group_id')
            self.tag.delete(group_ids)
            assert r.status_code == 200
            assert r.json()['errcode'] == 0
            # 获取标签列表，查看列表中是否没有了已删除的标签
            r = self.tag.list()
            assert not r.json()['tag_group']
        else:
            print('没有可删除的标签')

    @allure.story('测试删除不存在的标签')
    def test_del_fail(self):
        r = self.tag.delete('xxxxxxxxxx')
        assert r.status_code == 200
        assert r.json()['errcode'] == 40068
