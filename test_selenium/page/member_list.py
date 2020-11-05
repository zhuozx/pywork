from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class MemberList(BasePage):

    # 获取成员列表姓名
    def get_member_name(self):
        membername = []
        elements = self.driver.find_elements(By.XPATH, '//*[@id="member_list"]/tr/td[2]/span')
        for element in elements:
            membername.append(element.text)
        return membername