from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


# 基础页面类
class BasePage:
    _base_url = ''

    def __init__(self, driver: WebDriver = None):
        self.driver = ''
        if driver is None:
            # 打开一个新的谷歌浏览器窗口
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(3)

            # 复用现有谷歌浏览器窗口
            # chrome_arg = Options()
            # chrome_arg.debugger_address = '127.0.0.1:9222'
            # self.driver = webdriver.Chrome(options=chrome_arg)
            # self.driver.implicitly_wait(3)
        else:
            self.driver = driver
        if self._base_url != '':
            self.driver.get(self._base_url)

    # 封装元素定位方法
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    # 封装查找一组元素
    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)
