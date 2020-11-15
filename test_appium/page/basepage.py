import json
import logging
import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    # 黑名单，存放系统弹窗，应用升级提示等弹窗
    _black_list = []
    # 当前错误次数
    _error_count = 0
    # 最大错误次数
    _error_max = 10
    # send操作所需的数据
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # 封装查找元素方法，并加入黑名单处理机制
    def find(self, by, locator=None):
        logging.info('find:')
        logging.info(by)
        logging.info(locator)
        # 如果传入的是元组，则调用find_elements，否则，调用find_element
        try:
            element = self.driver.find_elements(*by) if isinstance(by, tuple) else self.driver.find_element(by, locator)
            self._error_count = 0
            return element
        # 如果没有定位到元素，则走此流程，用于处理_black_list中的弹窗
        except Exception as e:
            # 定位元素异常，则错误次数加1
            # 如果错误次数达到定义的最大数，则抛出异常
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e
            # 对黑名单中的数据进行遍历
            # 如果定位到黑名单中的元素，则进行点击操作，并再次进行页面流程中的元素定位
            for black in self._black_list:
                elements = self.driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(by, locator)
            # 遍历结束，还是没有找到元素，则抛出异常
            raise e

    # 加载yaml文件进行测试步骤驱动
    def steps(self, path, name):
        logging.info('steps:')
        logging.info(path)
        logging.info(name)
        # 获取yaml文件中的定位相关内容
        with open(path, encoding='utf-8') as f:
            steps: list[dict] = yaml.safe_load(f)[name]
        # 将steps转成字符串格式，并对{}这种参数化的数据进行替换
        content = json.dumps(steps)
        for param in self._params:
            content = content.replace('{' + param + '}', self._params[param])
        steps = json.loads(content)
        logging.info(steps)
        # 进行遍历，对每一组定位进行拆分
        for step in steps:
            logging.info(step['by'] + ' ' + step['locator'])
            if 'by' in step.keys():
                # 对于不同的action，有不同的操作
                by = (step['by'], step['locator'])
                if 'action' in step.keys():
                    if step['action'] == 'click':
                        self.find(*by).click()
                    elif step['action'] == 'send':
                        content: str = step['value']
                        self.find(*by).send_keys(step['value'])
                    elif step['action'] == 'getText':
                        return self.find(*by).text
                    elif step['action'] == 'finds':
                        elements = self.find(by)
                        return len(elements)
                    elif step['action'] == 'finds_click':
                        self.find(by)[0].click()
