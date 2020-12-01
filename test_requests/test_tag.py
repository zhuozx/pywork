import pytest
import requests
import yaml

from test_requests.tag import Tag


class TestTag:
    def setup_class(self):
        self.tag = Tag()
        self.tag.get_token()

    def test_list(self):
        self.tag.list()

    @pytest.mark.parametrize('tag',yaml.safe_load(open('tag.yaml')))
    def test_add(self,tag):
        print(tag)
        r = self.tag.add(tag['group_id'],tag['tag_names'])
        print(r)
        assert r.status_code == 200