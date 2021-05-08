#封禁用户
from common.tools import WebTools
from common.readconfig import ReadConfig as R
from common.raiseout import raiseout
from util.log import mylog as m
from time import sleep
l=m.log()

class Block():
    def __init__(self):
        self.d = WebTools()
        self.d.Getwebpage(R().get_http('url'))
        l.info("进入主页".format(R().get_http('url')))
        self.d.driver.maximize_window()
        sleep(1)
    def block(self):
        self.d.Click("xpath",'//*[@id="app"]/div[1]/div[2]/section/div/a[8]/div/div/div[2]')
        l.info("进入国内社区")
        sleep(3)
        self.d.Current_handel()
        self.d.switch_window("社区")
        self.d.Click('xpath', '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[3]/li/div')
        l.info("进入用户管理")
        sleep(1)
        self.d.WebDriverWait(30,0.5,'//*[@id="app"]/div/div[1]/div[1]/div/ul/div[3]/li/ul/div[1]/a/li')
        self.d.Click('xpath','//*[@id="app"]/div/div[1]/div[1]/div/ul/div[3]/li/ul/div[1]/a/li')
        l.info("进入用户列表")
        self.d.Click('xpath','//*[@id="app"]/div/div[2]/section/div/section/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button')
        l.info('选择用户，点击操作')
        sleep(2)
        try:
            self.d.Click('xpath','//*[@id="el-tooltip-3593"]')
            sleep(2)
            l.info("点击禁言")
            self.d.Click('xpath','//*[@id="app"]/div/div[2]/section/div/section/div[4]/div/div[3]/div/button[2]')
            sleep(1)
            l.info('点击确认')
            m=self.d.Check_element('xpath','/html/body/div[9]/p').text()
            l.info(m)
            return m
        except Exception:
            l.error("测试失败")
            self.d.get_windows_img()
            raiseout()

Block=Block()


