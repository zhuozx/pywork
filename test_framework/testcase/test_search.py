import pytest
import yaml
from test_framework.page.web import Web


class TestSearch:

    def setup(self):
        self.web = Web().open_browser()

    def teardown(self):
        self.web.close_browser()

    @pytest.mark.parametrize('keyword', yaml.safe_load(open('../data/search.yaml'))['testdata'])
    def test_search(self, keyword):
        result = self.web.goto_main().search(keyword)
        assert keyword in result
