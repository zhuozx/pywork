import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test_selenium.page.base_page import BasePage
from test_selenium.page.member_list import MemberList


# 添加成员页面
class AddMember(BasePage):
    # 添加成员
    def add_member(self):
        # 随机一个数字，用于动态化姓名等
        num = random.randint(1, 99999)
        self.name = '卓' + str(num)
        # 姓名
        self.find(By.ID, 'username').send_keys(self.name)

        # 别名
        self.find(By.ID, 'memberAdd_english_name').send_keys('test' + str(num))

        # 帐号
        self.find(By.ID, 'memberAdd_acctid').send_keys('ID' + str(num))

        # 性别选女
        self.find(By.XPATH, '//*[@class="member_edit_formWrap "]/div[1]/div[3]/div[2]/label[2]').click()

        # 手机选择香港，并填写号码
        self.find(By.CSS_SELECTOR, '.ww_telInput_zipCode_input').click()
        self.find(By.CSS_SELECTOR, '[data-value="852"]').click()
        self.find(By.ID, 'memberAdd_phone').send_keys('199' + str(random.randint(11111111, 99999999)))

        # 座机
        self.find(By.ID, 'memberAdd_telephone').send_keys('020-' + str(random.randint(11111111, 99999999)))

        # 邮箱
        self.find(By.ID, 'memberAdd_mail').send_keys(str(num) + '@qq.com')

        # 地址
        self.find(By.ID, 'memberEdit_address').send_keys("测试地址")

        # 点击部门选项的【修改】按钮
        self.find(By.CSS_SELECTOR, '[class="ww_groupSelBtn_add js_show_party_selector"]').click()
        # 在弹窗中输入关键字搜索部门并选中
        self.find(By.CSS_SELECTOR, '.multiPickerDlg_search input').click()
        self.find(By.CSS_SELECTOR, '.multiPickerDlg_search input').send_keys("测试中心")
        # 添加显示等待条件，等待查询结果出现后再点击
        self.wait_for_click(By.CSS_SELECTOR, '#searchResult li').click()
        # self.find(By.CSS_SELECTOR, '#searchResult li').click()

        # 在弹窗中点击确定按钮
        self.find(By.XPATH, '//*[@class="qui_dialog_foot ww_dialog_foot"]/a[1]').click()
        # 职务
        self.find(By.ID, 'memberAdd_title').send_keys('技术主管')
        # 身份选择上级
        self.find(By.CSS_SELECTOR, '.js_identity_stat').click()

        # 对外信息-职务，选自定义
        self.find(By.CSS_SELECTOR, '[value=custom]').click()
        self.find(By.NAME, 'extern_position').send_keys("测试打工人")

        # 取消发送邀请
        self.find(By.CSS_SELECTOR, '[name="sendInvite"]').click()

        # 点击页面底部的保存按钮
        self.find(By.XPATH, '//*[@class="js_member_editor_form"]/div[3]/a[2]').click()
        return MemberList(self.driver)

    # 判断添加的名字是不是在列表中
    def get_member_name(self, name):
        self.driver.execute_script('document.documentElement.scrollTop=0')
        while True:
            elements = self.find((By.XPATH, '//*[@id="member_list"]/tr/td[2]/span'))
            total_name = [element.text for element in elements]
            # 如果匹配到姓名，则结束循环，返回True
            if name in total_name:
                return True
            page_element: str = self.wait_for_click(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
            cur_page, total_page = page_element.split('/')
            # 如果不是最后一页，则点击下一页按钮，否则返回false
            if int(cur_page) == int(total_page):
                return False
            else:
                self.find(By.CSS_SELECTOR, '.js_next_page').click()
