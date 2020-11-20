from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from test_framework.page.basepage import BasePage
from test_framework.page.main_page import MainPage


class Web(BasePage):

    # 打开浏览器
    def open_browser(self):
        data = self.load_data('../data/web.yaml')
        # 根据配置的方式进行初始化，1表示打开新的浏览器，2表示复用现有浏览器
        if data['way'] == 1:
            # 根据不同的browser打开不同的浏览器，并打开url
            if data['browser'].lower() == 'chrome':
                self.driver = webdriver.Chrome()
            elif data['browser'].lower() == 'firefox':
                self.driver = webdriver.Firefox()
            self.driver.maximize_window()
        elif data['way'] == 2:
            # 复用现有谷歌浏览器窗口
            chrome_arg = Options()
            chrome_arg.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=chrome_arg)

        self.driver.implicitly_wait(3)
        self.driver.get(data['url'])

        return self

    # 关闭浏览器
    def close_browser(self):
        self.driver.quit()

    # 进入首页
    def goto_main(self):
        return MainPage(self.driver)
