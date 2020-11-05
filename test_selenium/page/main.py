import shelve
from selenium.webdriver.common.by import By
from test_selenium.page.base_page import BasePage
from test_selenium.page.member_add import AddMember
from test_selenium.page.member_list import MemberList


# 首页
class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame/'

    # 保存cookies
    def save_cookies(self):
        db = shelve.open("cookies")
        db['cookies'] = self.driver.get_cookies()
        db.close()

    # 使用cookie登录
    def login_with_cookies(self):
        db = shelve.open("cookies")
        cookies = db['cookies']
        db.close()
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    # 点击首页的【添加成员】按钮跳转到添加成员页面
    def goto_add_member(self):
        # 滑动到页面底部
        self.driver.execute_script('document.documentElement.scrollTop=1000')
        # 点击添加成员按钮
        self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        # 进入添加成员页面
        return AddMember(self.driver)

    # 点击【通讯录】按钮进入通讯录页面
    def goto_member_list(self):
        self.find(By.ID, 'menu_contacts').click()
        return MemberList(self.driver)
