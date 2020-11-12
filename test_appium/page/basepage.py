import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    # 黑名单
    _black_list = []
    # 当前错误次数
    _error_count = 0
    # 最大错误次数
    _error_max = 10
    # send操作所需的数据
    params = {}

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator=None):
        # 如果传入的是元组，则调用find_elements，否则，调用find_element
        try:
            element = self.driver.find_elements(*by) if isinstance(by, tuple) else self.driver.find_element(by, locator)
            self._error_count = 0
            return element
        #以下内容是录播课的，能明白逻辑，但还没有实验过
        except Exception as e:
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e
            for black in self._black_list:
                elements = self.driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(by, locator)
            raise e

    def steps(self, path, name):
        # 获取yaml文件中的定位相关内容
        with open(path, encoding='utf-8') as f:
            steps: list[dict] = yaml.safe_load(f)[name]
        # 进行遍历，对每一组定位进行拆分
        for step in steps:
            if 'by' in step.keys():
                # 对于不同的action，有不同的操作
                if 'action' in step.keys():
                    if step['action'] == 'click':
                        self.find(step['by'], step['locator']).click()
                    elif step['action'] == 'send':
                        content: str = step['value']
                        self.find(step['by'], step['locator']).send_keys(self.params[content])
                    elif step['action'] == 'getText':
                        return self.find(step['by'], step['locator']).text
                    elif step['action'] == 'finds':
                        elements = self.find((step['by'], step['locator']))
                        return len(elements)
                    elif step['action'] == 'finds_click':
                        self.find((step['by'], step['locator']))[0].click()
