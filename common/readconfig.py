#coding=utf-8
import configparser
import codecs,os

proDir = os.path.split(os.path.realpath(__file__))[0]
prj=os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir))
configpath = os.path.join(prj,"config" ,"config.ini")
#日志路径
log_path=os.path.join(prj,"util","log")

#报告路径
report_path=os.path.join(prj,'util','report')

#截图路径
screet_path=os.path.join(prj,"util",'screet')

class ReadConfig:
    """
    专门读取配置文件的，.ini文件格式
    """
    def __init__(self):
        fd = open(configpath)
        data = fd.read()
        # remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            files = codecs.open(configpath, "w")
            files.write(data)
            files.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)

    def get_http(self, name):
        value = self.cf.get("http", name)
        return value

r=ReadConfig()