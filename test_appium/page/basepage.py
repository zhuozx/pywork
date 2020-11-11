import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _black_list = []
    _error_count = 0
    _error_max = 10
    params = {}

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator=None):
        try:
            element = self.driver.find_elements(*by) if isinstance(by, tuple) else self.driver.find_element(by, locator)
            self._error_count = 0
            return element
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

    def steps(self, path):
        with open(path, encoding='utf-8') as f:
            steps: list[dict] = yaml.safe_load(f)
        for step in steps:
            if 'by' in step.keys():
                if 'action' in step.keys():
                    if step['action'] == 'click':
                        self.find(step['by'], step['locator']).click()
                    if step['action'] == 'send':
                        content: str = step['value']
                        print('替换前'+content)
                        self.find(step['by'], step['locator']).send_keys(self.params[content])
