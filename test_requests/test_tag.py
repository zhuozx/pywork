import pytest
from test_requests.tag import Tag

data = {
    'normal':[['group_name1',['tag_name1','tag_name2']]],
    'fail':[['group_name1',['tag_nameAAAAAAAAAAAAAAAAAAAAAAAAA']]]
}

class TestTag:
    def setup_class(self):
        self.tag = Tag()
        self.tag.get_token()

    def test_get_list(self, tag_id=None):
        r = self.tag.list(tag_id)

    def delete(self, group_id):
        return self.tag.delete(group_id)

    @pytest.mark.parametrize('group_name,tag_names', data['normal'])
    def test_add(self, group_name, tag_names):
        r = self.tag.add(group_name, tag_names)
        print(r)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        assert group_name == r.json()['tag_group']['group_name']
        # assert tag_names['tag_names'] in r.json()['tag_group']['tag']['name']

    # @pytest.mark.parametrize('group_id', [['etFo4LBwAADYjhS89I7XFh2N9knYcsUA']])
    def test_del(self, group_id):
        r = self.delete(group_id)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    def test_add_fail(self, tag):
        print(tag)
