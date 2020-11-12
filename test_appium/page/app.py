from appium import webdriver

from test_appium.page.basepage import BasePage
from test_appium.page.main import Main


class App(BasePage):
    def start(self):
        _appPackage = 'com.tencent.wework'
        _appActivity = '.launch.LaunchSplashActivity'
        # 如果当前driver为空，则初始化一个driver
        if self.driver == None:
            caps = {}
            caps['platformName'] = 'Android'
            caps['deviceName'] = 'hogwarts'
            caps['appPackage'] = _appPackage
            caps['appActivity'] = _appActivity
            caps['noReset'] = 'true'
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
            self.driver.implicitly_wait(10)

        return self

    def main(self):
        return Main(self.driver)
