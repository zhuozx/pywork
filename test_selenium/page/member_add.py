import random
import time

from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.member_list import MemberList


class AddMember(BasePage):
    # 添加成员
    def add_member(self):
        num = random.randint(1, 99999)
        self.name = '名字' + str(num)
        # 姓名
        self.find(By.ID, 'username').send_keys(self.name)

        # 别名
        self.find(By.ID, 'memberAdd_english_name').send_keys('test' + str(random.randint(1, 99999)))

        # 帐号
        self.find(By.ID, 'memberAdd_acctid').send_keys('ID' + str(random.randint(1, 99999)))

        # 性别选女
        self.find(By.XPATH, '//*[@class="member_edit_formWrap "]/div[1]/div[3]/div[2]/label[2]').click()

        # 手机选择香港，并填写号码
        self.find(By.CSS_SELECTOR, '.ww_telInput_zipCode_input').click()
        self.find(By.CSS_SELECTOR, '[data-value="852"]').click()
        self.find(By.ID, 'memberAdd_phone').send_keys(str(random.randint(11111111111,99999999999)))

        # 座机
        self.find(By.ID, 'memberAdd_telephone').send_keys('020-'+str(random.randint(11111111,99999999)))

        # 邮箱
        self.find(By.ID, 'memberAdd_mail').send_keys(str(random.randint(1, 99999)) + '@qq.com')

        # 地址
        self.find(By.ID, 'memberEdit_address').send_keys("测试地址")

        # 点击部门选项的【修改】按钮
        self.find(By.CSS_SELECTOR, '[class="ww_groupSelBtn_add js_show_party_selector"]').click()
        # 在弹窗中输入关键字搜索部门并选中
        self.find(By.CSS_SELECTOR, '.multiPickerDlg_search input').click()
        self.find(By.CSS_SELECTOR, '.multiPickerDlg_search input').send_keys("测试中心")
        self.find(By.CSS_SELECTOR, '#searchResult li').click()

        # 在弹窗中点击确定按钮
        self.find(By.XPATH, '//*[@class="qui_dialog_foot ww_dialog_foot"]/a[1]').click()

        # 身份选择上级
        self.find(By.CSS_SELECTOR, '[class="ww_radio js_identity_stat"]').click()

        # 对外信息-职务，选自定义
        self.find(By.CSS_SELECTOR, '[value=custom]').click()
        self.find(By.NAME, 'extern_position').send_keys("测试打工人")

        # 取消发送邀请
        self.find(By.CSS_SELECTOR, '[name="sendInvite"]').click()

        # 点击页面底部的保存按钮
        self.find(By.XPATH, '//*[@class="js_member_editor_form"]/div[3]/a[2]').click()
        return MemberList(self.driver)
