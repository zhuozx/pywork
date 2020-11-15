from appium import webdriver
from test_appium.page.basepage import BasePage
from test_appium.page.main import Main


class App(BasePage):
    def start(self):
        _appPackage = 'com.tencent.wework'
        _appActivity = '.launch.LaunchSplashActivity'
        # 如果当前driver为空，则初始化一个driver
        if self.driver is None:
            caps = {}
            caps['platformName'] = 'Android'
            caps['deviceName'] = 'hogwarts'
            caps['appPackage'] = _appPackage
            caps['appActivity'] = _appActivity
            caps['noReset'] = 'true'
            # 建立客户端与服务端的连接
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
            self.driver.implicitly_wait(10)
        else:
            # 启动app, 启动的页面是caps里设置的activity
            self.driver.launch_app()

        return self

    def stop(self):
        self.driver.quit()

    # 进入app首页
    def main(self):
        return Main(self.driver)
