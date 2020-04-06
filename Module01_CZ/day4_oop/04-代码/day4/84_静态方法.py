"""
演示静态方法
"""
class Chinese:
    country = "中国"
    def __init__(self,id_num,name):
        self.id_num = id_num
        self.name = name

    @staticmethod
    def show():
        print("今天天气不错")

def show():
    print("今天天气不错")

c = Chinese("4102041999909091011","张大帅")
show()

