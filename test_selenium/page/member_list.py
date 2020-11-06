from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


# 通讯录页面
class MemberList(BasePage):

    # 获取成员列表姓名，将姓名保存到一个数组里面
    def get_member_name(self):
        membername = []
        elements = self.finds(By.XPATH, '//*[@id="member_list"]/tr/td[2]/span')
        for element in elements:
            membername.append(element.text)
        return membername

    # 删除列表第一个成员
    def del_member(self):
        # 勾选列表第一条
        self.find(By.XPATH, '//*[@id="member_list"]/tr[1]/td[1]').click()
        # 点击删除按钮
        self.find(By.XPATH, '//*[@class="ww_operationBar"]/a[3]').click()
        # 点击确定删除
        self.find(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]').click()
        return True
