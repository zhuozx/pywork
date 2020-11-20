import yaml
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def load_data(self, path):
        with open(path, encoding='utf-8') as f:
            return yaml.safe_load(f)

    def find(self, by, locator=None):
        if isinstance(by, tuple):
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_element(by, locator)

    def steps(self, path):
        steps = self.load_data(path)['steps']
        # 对steps进行遍历
        for step in steps:
            if 'by' in step:
                # 如果是click操作，则定位元素并点击
                if 'click' == step['action']:
                    self.find(step['by'], step['locator']).click()
                # 如果是send操作，则定位元素并输入
                if 'send' == step['action']:
                    # 提取value对应的参数化变量，并匹配在_params中对应的内容
                    # 由于yaml中参数化的格式固定为${xxx}，截断${}
                    content = self._params[step['value'][2:-1]]
                    self.find(step['by'], step['locator']).send_keys(content)
                # 如果是get操作，则获取元素的文本并返回
                if 'get' == step['action']:
                    return self.find(step['by'], step['locator']).text
