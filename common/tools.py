import os
import sys
import time
Path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(Path)[0]
sys.path.append(rootPath)
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from common import readconfig  as R
# ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# sys.path.append(ROOT_DIR)


class WebTools(object):
    def __init__(self):
        self.driver=self.openbrowser()

    # 打开浏览器的方法
    def openbrowser(self, browser='chrome'):
        try:
            if browser == 'chrome':
                driver = webdriver.Chrome()
            elif browser == 'firefox':
                driver = webdriver.Firefox()
            elif browser == 'ie':
                driver = webdriver.Ie()
            else:
                driver = webdriver.Edge()
            time.sleep(1)
            return driver
        except:
            print("open browser fail!")
            return None
    # 跳转页面
    def Getwebpage(self, url):
        self.driver.get(url)



    # 浏览器前进操作
    def forward(self):
        self.driver.forward()

    # 浏览器后退操作
    def back(self):
        self.driver.back()

    def close(self):
        self.driver.close()


    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    # 显性等待时间
    def WebDriverWait(self, MaxTime, Mimtime, value):
        element = self.driver.find_element(By.XPATH, value)
        WebDriverWait(self.driver, MaxTime, Mimtime).until(lambda ele:element)


    # 保存图片
    def get_windows_img(self):
        file_path = R.screet_path
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            print("截图已保存在："+file_path)
        except NameError as e:
            self.get_windows_img()

    def Current_handel(self):
        # 切换到新窗口
        all_handles = self.driver.window_handles
        for handle in all_handles:
            self.driver.switch_to.window(handle)

    def switch_window(self, windowname):
        all_handles = self.driver.window_handles
        for handle in all_handles:
            self.driver.switch_to.window(handle)  # 切换到该句柄
            if self.driver.title == windowname:  # 如果该窗口的title是windowname
                self.driver.switch_to.window(handle)  # 切换
                break

    def iframe(self,ele):
        self.driver.switch_to.frame (ele)
        time.sleep(2)

    def frameback(self):
        self.driver.switch_to.default_content()

    # 输入内容方法
    def Input(self, type, value, inputvalue):
        if type == "xpath":
            self.driver.find_element_by_xpath(value).send_keys(inputvalue)
        elif type == "class_name":
            self.driver.find_element_by_class_name(value).send_keys(inputvalue)
        elif type == "id":
            self.driver.find_element_by_id(value).send_keys(inputvalue)
        elif type == "name":
            self.driver.find_element_by_name(value).send_keys(inputvalue)
        elif type == "link_text":
            self.driver.find_element_by_link_text(value).send_keys(inputvalue)
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value).send_keys(inputvalue)

    # 鼠标事件方法一
    def Click(self, type, value):
        if type == "xpath":
            self.driver.find_element_by_xpath(value).click()
        elif type =="seletcor":
            self.driver.find_element_by_css_selector(value).click()
        elif type == "class_name":
            self.driver.find_element_by_class_name(value).click()
        elif type == "id":
            self.driver.find_element_by_id(value).click()
        elif type == "name":
            self.driver.find_element_by_name(value).click()
        elif type == "link_text":
            self.driver.find_element_by_link_text(value).click()
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value).click()

    # 鼠标事件方法二
    def Clear(self, type, value):
        if type == "xpath":
            self.driver.find_element_by_xpath(value).clear()
        elif type == "id":
            self.driver.find_element_by_id(value).clear()
        elif type == "name":
            self.driver.find_element_by_name(value).clear()
        elif type == "link_text":
            self.driver.find_element_by_link_text(value).clear()
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value).clear()

    # 验证元素是否存在
    def Check_element(self, type, value):
        if type == "xpath":
            self.driver.find_element_by_xpath(value)
        elif type == "id":
            self.driver.find_element_by_id(value)
        elif type == "name":
            self.driver.find_element_by_name(value)
        elif type == "link_text":
            self.driver.find_element_by_link_text(value)
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value)

    # 获取子元素
    def Select_child_elements(self, type, value1, value2):
        if type == "xpath":
            Select(self.driver.find_element_by_xpath(value1)).select_by_visible_text(value2)
        elif type == "id":
            Select(self.driver.find_element_by_id(value1)).select_by_visible_text(value2)
        elif type == "name":
            Select(self.driver.find_element_by_name(value1)).select_by_visible_text(value2)
        elif type == "link_text":
            Select(self.driver.find_element_by_link_text(value1)).select_by_visible_text(value2)
        elif type == "partial_link_text":
            Select(self.driver.find_element_by_partial_link_text(value1)).select_by_visible_text(value2)

    # 获取输入框的值
    def Get_attribute(self, type, value1, value2):
        if type == "xpath":
            Value = self.driver.find_element_by_xpath(value1).get_attribute(value2)
            return Value
        elif type == "name":
            Value = self.driver.find_element_by_name(value1).get_attribute(value2)
            return Value
        elif type == "link_text":
            Value = self.driver.find_element_by_link_text(value1).get_attribute(value2)
            return Value
        elif type == "class_name":
            Value = self.driver.find_element_by_class_name(value1).get_attribute(value2)
            return Value
        elif type == "id":
            Value = self.driver.find_element_by_id(value1).get_attribute(value2)
            return Value

    # 获取下拉框的文本的值
    def Get_text(self, type, value):
        if type == "xpath":
            text = self.driver.find_element_by_xpath(value).text
            return text
        elif type == "name":
            text = self.driver.find_element_by_name(value).text
            return text
        elif type == "link_text":
            text = self.driver.find_element_by_link_text(value).text
            return text
        elif type == "class_name":
            text = self.driver.find_element_by_class_name(value).text
            return text
        elif type == "id":
            text = self.driver.find_element_by_id(value).text
            return text


    # 鼠标移动点击机制
    def Move_action(self, type, value):
        if type == "xpath":
            xm = self.driver.find_element_by_xpath(value)
            webdriver.ActionChains(self.driver).click(xm).perform()
        elif type == "id":
            xm = self.driver.find_element_by_id(value)
            webdriver.ActionChains(self.driver).click(xm).perform()
        elif type == "name":
            xm = self.driver.find_element_by_name(value)
            webdriver.ActionChains(self.driver).click(xm).perform()
        elif type == "link_text":
            xm = self.driver.find_element_by_link_text(value)
            webdriver.ActionChains(self.driver).click(xm).perform()

    #鼠标双击
    def double_click(self,type,value):
        ele=self.driver.find_element_by_xpath(value)


    # 校验按钮是否为选中状态
    def Is_selected(self, type, value):
        if type == "id":
            self.driver.find_element_by_id(value).is_selected()
        elif type == "xpath":
            self.driver.find_element_by_xpath(value).is_selected()
        elif type == "class_name":
            self.driver.find_element_by_class_name(value).is_selected()
        elif type == "name":
            self.driver.find_element_by_name(value).is_selected()
        elif type == "link_text":
            self.driver.find_element_by_link_text(value).is_selected()

    #上传附件
    def send(self,file,path):
        upload = self.driver.find_element_by_name(file)
        time.sleep(3)
        upload.send_keys(path)
