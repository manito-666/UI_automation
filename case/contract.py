#社区动态审核
from common.tools import WebTools
from common.readconfig import ReadConfig as R
from common.raiseout import raiseout
from util.log import mylog as m
from time import sleep
l=m.log()

class Check():
    def __init__(self):
        self.d = WebTools()
        self.d.Getwebpage(R().get_http('url'))
        l.info("进入主页".format(R().get_http('url')))
        self.d.driver.maximize_window()
        sleep(1)
    def check(self):
        self.d.Click("xpath",'//*[@id="app"]/div[1]/div[2]/section/div/a[7]/div/div/div[2]')
        l.info("进入国内社区")
        sleep(3)
        self.d.Current_handel()
        self.d.switch_window("社区")
        self.d.Click('xpath','//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/li/div')
        l.info("点击舆论管理")
        sleep(1)
        self.d.WebDriverWait(30,1,'//*[@id="publicAuditTitle"]')
        self.d.Click("xpath",'//*[@id="publicAuditTitle"]')
        l.info("点击动态审核")
        sleep(2)
        self.d.Click("xpath",'//*[@id="app"]/div/div[2]/section/div/section[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/div/button')
        l.info("点击操作")
        sleep(2)
        # self.d.WebDriverWait(30,0.5,'//*[contains(@class,"el-dropdown-menu__item")]')
        self.d.Click("selector",'//*[contains(@class,"el-dropdown-menu__item")]')
        sleep(2)
        l.info("点击同意")
        try:
            self.d.Click('xpath','/html/body/div[3]/div/div[3]/button[2]')
            l.info("点击确定")
            self.d.WebDriverWait(30,0.5,'/html/body/div[5]')
            r=self.d.Click('xpath','/html/body/div[5]').text()
            l.info(r)
            self.d.close()
            return r
        except Exception:
            l.error("审核失败")
            self.d.get_windows_img()
            raiseout()
m=Check()
if __name__ == '__main__':
    m.check()