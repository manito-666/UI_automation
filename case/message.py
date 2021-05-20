#游戏社区发布资讯
import os,sys
from common.tools import WebTools
from common.readconfig import r
from common.raiseout import raiseout
from util.log import mylog as m
from time import sleep
l=m.log()

class community:
    def __init__(self):
        self.d = WebTools()
        self.d.Getwebpage(r.get_http('url'))
        l.info("进入主页==>> {}".format(r.get_http('url')))
        self.d.driver.maximize_window()
        sleep(2)
    def send(self):   #发布资讯
        self.d.Click("xpath", '//*[@id="app"]/div[1]/div[2]/section/div/a[6]/div/div/div[2]')
        l.info("进入国内社区")
        self.d.Current_handel()
        self.d.switch_window("游戏社区Admin")
        sleep(1)
        self.d.Click('xpath','//*[@id="app"]/div/div[2]/section/div/section/form/div[8]/div/div/button')
        l.info("发布资讯")
        sleep(2)
        self.d.WebDriverWait(30, 0.5, '//*[contains(@class,"el-dropdown-menu__item text_c")]')
        self.d.Click('xpath','//*[contains(@class,"el-dropdown-menu__item text_c")]')
        sleep(1)
        self.d.Input('xpath','//*[@id="app"]/div/div[2]/section/div/form/div[1]/div/div/input',"lpl")
        l.info("输入标题:".format("lpl"))
        sleep(1)
        self.d.Click('xpath','//*[@id="app"]/div/div[2]/section/div/form/div[2]/div/div/div[1]/span/span/i')
        sleep(1)
        self.d.Click('xpath','/html/body/div[2]/div[1]/div[1]/ul/li')
        l.info('选择发布人')
        # self.d.Click('xpath','//*[@id="app"]/div/div[2]/section/div/form/div[3]/div/div/div[1]/span/span/i')
        # sleep(2)
        # self.d.WebDriverWait(30, 0.5,'/html/body/div[4]/div[1]/div[1]/ul/li[2]')
        # self.d.Click('xpath','/html/body/div[4]/div[1]/div[1]/ul/li[2]')
        # l.info('选择文章类型')
        self.d.Click('xpath','//*[@id="app"]/div/div[2]/section/div/form/div[5]/div/div/div/label[1]/span[1]/span')
        l.info("选择文章状态")
        self.d.send('file','/Users/wangzhipeng/Downloads/photo/4af7ffde5e59adc020af3c4dad959417edfaa843.jpg')
        sleep(3)
        l.info("上传封面")

        self.d.iframe('xpath',"//*[starts-with(@id,'vue-tinymce')]")
        sleep(2)
        l.info("进入富文本")
        self.d.Click('xpath','//*[@id="tinymce"]')
        sleep(1)
        self.d.WebDriverWait(30,0.5,'//*[@id="tinymce"]/p')
        self.d.Input('id','tinymce','先知召唤达标,活动期间，使用先知宝珠可获得积分，当积分达到一定数额即可获得对应奖励')
        l.info("输入内容")
        sleep(1)
        # self.d.Click('xpath','//*[@id="app"]/div/div[2]/section/div/form/div[8]/div/div/div[2]/div/button')
        # sleep(1)
        # self.d.send('file','/Users/wangzhipeng/Downloads/photo/7900126941261_098f6bcd.jpeg')
        # sleep(5)
        self.d.frameback()
        sleep(2)
        try:
            self.d.WebDriverWait(30,0.5,'//*[@id="app"]/div/div[2]/section/div/form/div[9]/div/button[1]')
            self.d.Click('xpath','//*[@id="app"]/div/div[2]/section/div/form/div[9]/div/button[1]')
            l.info("点击创建文章")
            # self.d.WebDriverWait(30,0.5,'/html/body/div[3]')
            # r=self.d.Check_element('xpath','/html/body/div[3]')
            r="保存文章成功"
            l.info("保存文章成功")
            self.d.close()
            return r
        except Exception as e:
            l.error("添加失败: " + format(e))
            self.d.get_windows_img()
            raiseout()

community=community()

