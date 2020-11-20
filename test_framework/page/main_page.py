from test_framework.page.basepage import BasePage


class MainPage(BasePage):

    # 进行搜索
    def search(self,key):
        self._params['keyword'] = key
        return self.steps('../data/search.yaml')