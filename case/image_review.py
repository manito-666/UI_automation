#社区动态审核
from common.tools import WebTools
from common.readconfig import ReadConfig as R
from common.raiseout import raiseout
from util.log import mylog as m
from time import sleep
l=m.log()

class Review():
    def __init__(self):
        self.d = WebTools()
        self.d.Getwebpage(R().get_http('url'))
        l.info("进入主页".format(R().get_http('url')))
        self.d.driver.maximize_window()
        sleep(1)
    def review(self):
        self.d.Click("xpath",'//*[@id="app"]/div[1]/div[2]/section/div/a[2]/div/div/div[2]')
        l.info("进入国内社区")
        sleep(3)
        self.d.Current_handel()
        self.d.switch_window("社区")
        self.d.Click('xpath','//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/li/div')
        l.info("点击舆论管理")
        sleep(1)
        self.d.Click('xpath','//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/li/ul/div[3]/a/li')
        l.info("点击图片审核")
        sleep(1)
        try:
            self.d.WebDriverWait(30,0.5,'//*[@id="app"]/div/div[2]/section/div/section[2]/ul/li[1]/div[2]/div[2]/div[3]/i')
            self.d.Click('xpath','//*[@id="app"]/div/div[2]/section/div/section[2]/ul/li[1]/div[2]/div[2]/div[3]/i')
            self.d.WebDriverWait(30, 0.5, '/html/body/div[6]')
            m=self.d.Check_element('xpath','/html/body/div[6]').text()
            l.info(m)
            return m
        except Exception:
            l.error("测试失败")
            self.d.get_windows_img()
            raiseout()


m=Review()


