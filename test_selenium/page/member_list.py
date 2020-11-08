from selenium.webdriver.common.by import By
from test_selenium.page.base_page import BasePage


# 通讯录页面
class MemberList(BasePage):
    # 删除列表第一个成员
    def del_member(self):
        # 勾选列表第一条
        del_name = self.find(By.XPATH, '//*[@ID="member_list"]/tr[1]/td[2]/span[1]').text
        self.find(By.XPATH, '//*[@id="member_list"]/tr[1]/td[1]').click()
        # 点击删除按钮
        self.find(By.XPATH, '//*[@class="ww_operationBar"]/a[3]').click()
        # 点击确定删除
        self.find(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]').click()
        tip: str = self.wait_for_click(By.ID, 'js_tips').text
        self.search(del_name)

    # 搜索用户
    def search(self, name):
        self.find(By.ID, 'memberSearchInput').send_keys(name)
        #如果查询到结果，说明存在该用户，返回False；否则，返回True
        if self.find(By.CSS_SELECTOR, '.ww_commonCntHead_title_inner_text').is_displayed():
            return False
        else:
            return True

