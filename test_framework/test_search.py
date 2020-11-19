import time

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


def load_data(path):
    with open(path) as f:
        return yaml.safe_load(f)


class TestSearch:
    _params = {}

    def test_load_data(self):
        steps = load_data('test_search.yaml')['steps']
        for step in steps:
            if 'send' == step['action']:
                print(step['value'][2:-1])


    def setup(self):
        # 读取yaml文件中的browser和url
        browser = load_data('test_search.yaml')['browser']
        url = load_data('test_search.yaml')['url']
        # 根据不同的browser打开不同的浏览器，并打开url
        if browser.lower() == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get(url)

    def steps(self):
        # 读取yaml文件中的steps
        steps: list[dict] = load_data('test_search.yaml')['steps']
        # 对steps进行遍历
        for step in steps:
            if 'by' in step:
                # 如果发现是click，则定位元素并点击
                if 'click' == step['action']:
                    self.driver.find_element(step['by'], step['locator']).click()
                # 如果发现是send操作，则定位元素并输入
                if 'send' == step['action']:
                    # 提取value对应的参数化变量，并匹配在_params中对应的内容
                    # 由于yaml中参数化的格式固定为${xxx}，截断${}
                    content = self._params[step['value'][2:-1]]
                    self.driver.find_element(step['by'], step['locator']).send_keys(content)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('keyword', load_data("test_search.yaml")['testdata'])
    def test_search(self, keyword):
        # 保存搜索内容到字典中，以便操作步骤中用
        self._params['keyword'] = keyword
        self.steps()
