"""
演示类方法
"""
class Chinese:
    country = "中国"
    def __init__(self,id_num,name):
        self.id_num = id_num
        self.name = name

    # @classmethod
    # def show_country(cls):
    #     print("我是中国人")

    @classmethod
    def show_country(cls):
        """类方法调用实例的成员"""
        print("我是中国人")
        # print(self.name)
        # self.show()

    def show(self):
        """实例方法调用类的成员"""
        print(self.name)
        print(Chinese.country)
        Chinese.show_country()

# c = Chinese("410204199909091011","张大帅")
# Chinese.show_country()
# c.show_country()

"""演示实例方法中调用类的成员"""
# c = Chinese("410204199909091011","张大帅")
# c.show()

"""演示类方法中调用实例的成员"""
Chinese.show_country()