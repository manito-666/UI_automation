#coding=utf-8
import random
import string


class RanName():
    # 随机生成姓名：中文、英文、·默认长度2-10位
    def __init__(self, min_lenth=None, max_lenth=None):
        if min_lenth!=None:
            self.min_lenth = min_lenth
        else:
            self.min_lenth = 2
        if max_lenth!=None:
            self.max_lenth = max_lenth
        else:
            self.max_lenth = 10

    def chinese_char(self):
        #随机生成一个汉字
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xf9)  # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
        val = f'{head:x}{body:x}'
        str = bytes.fromhex(val).decode('gb2312')
        return (str)

    def chinese_str(self, num):
        #随机生成一个汉字字符串
        chars = []
        for i in range(num):
            chars.append(self.chinese_char())
        return (''.join(chars))

    def gen_random_name(self):
        #随机生成姓名：2-20个中英文字符
        return ''.join(
            random.choice(string.ascii_letters + self.chinese_str(5)) for _ in range(self.min_lenth, self.max_lenth))

    def gen_random_number(self):
        return random.randint(10000000,99999999)


if __name__=="__main__":
    g=RanName()
    print(g.gen_random_name())