"""
演示类方法理解误区
self cls 自动补充
"""
class Chinese:
    country = "中国"
    def __init__(self,id_num,name):
        self.id_num = id_num
        self.name = name
    @classmethod
    def show(cls):
        print(cls.name)

c = Chinese("4102041999909091011","张大帅")
c.show()