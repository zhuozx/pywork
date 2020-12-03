import allure
import pytest

from test_requests.tag import Tag

data = {
    'normal': [
        ['group_name1', ['tag_name1', 'tag_name2']],
        ['group_name2', ['tag_nameA', 'tag_nameB']],
    ],
    'fail': [
        ['group_name1', ['tag_nameeeeeeeeeeeeeeeeeeeeeeeee']],
        ['group_nameeeeeeeeeeeeeeeeeeeeee', ['tag_nameA']]
    ]
}


class TestTag:
    def setup_class(self):
        self.tag = Tag()
        self.tag.get_token()

    @allure.story('测试添加正常标签')
    @pytest.mark.parametrize('group_name,tag_names', data['normal'])
    def test_add(self, group_name, tag_names):
        # 添加标签
        r = self.tag.add(group_name, tag_names)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

        # 获取标签列表
        r = self.tag.list()
        # 获取报文中的所有tag_group字段
        tag_groups = [tag_group for tag_group in r.json()['tag_group']]
        # 获取测试数据所在报文节点的tag_group
        current_group = [tag_group for tag_group in tag_groups if tag_group['group_name'] == group_name]
        assert group_name in current_group[0]['group_name']

        # 获取测试数据group_name所在报文节点的tag下的所有name字段
        current_tags = [tag['name'] for tag in current_group[0]['tag']]
        # 判断测试数据中的tag_name是否在报文中
        for tag_name in tag_names:
            assert tag_name in current_tags

    @allure.story('测试添加超长标签')
    @pytest.mark.parametrize('group_name,tag_names', data['fail'])
    def test_add_fail(self, group_name, tag_names):
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
    @pytest.mark.parametrize('tag_id', [
        ['etFo4LBwAAzRd9HJLZI_dLtuI1OKjZbw', 'etFo4LBwAA3YjGEb8l2n79q6pmcb6mcw']
    ])
    def test_list_by_tag(self, tag_id):
        r = self.tag.list(tag_id)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        tags = r.json()['tag_group'][0]['tag']
        for tag in tags:
            assert tag['id'] in tag_id

    @allure.story('测试用不存在的tag_id查询标签')
    def test_list_fail(self):
        r = self.tag.list(['xxxxxxxxxx'])
        assert r.status_code == 200
        assert r.json()['errcode'] == 40068

    @allure.story('测试删除存在的标签')
    def test_del(self):
        group_id = []
        # 获取标签列表
        r = self.tag.list()
        # 对报文数据进行循环，找到测试数据中所有group_name对应的group_id
        for tag_group in r.json()['tag_group']:
            for test_data in data['normal']:
                if tag_group['group_name'] in test_data:
                    group_id.append(tag_group['group_id'])
        # 如果找到了要删除的group_id，则调用删除接口
        if group_id is not None:
            r = self.tag.delete(group_id)
            assert r.status_code == 200
            assert r.json()['errcode'] == 0

        # 获取标签列表，查看列表中是否没有了已删除的标签
        r = self.tag.list()
        current_group = [tag_group['group_name'] for tag_group in r.json()['tag_group']]
        for test_data in data['normal']:
            assert test_data[0] not in current_group

    @allure.story('测试删除不存在的标签')
    def test_del_fail(self):
        r = self.tag.delete('xxxxxxxxxx')
        assert r.status_code == 200
        assert r.json()['errcode'] == 40068
