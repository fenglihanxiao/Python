"""
演示类变量
"""
class Cat:
    subject = "猫科"
    def __init__(self, type, name):
        self.__type = type
        self.__name = name

    def get_type(self):
        return self.__type

    def set_type(self,type):
        self.__type = type

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

# cat1 = Cat("英格兰短毛猫","小短毛")
# # # 访问方式一：类名.类变量名(推荐)
# # print(Cat.subject)
# # # 访问方式二：对象名.类变量名(不推荐)
# # print(cat1.subject)
# # cat2 = Cat("波斯猫","大帅")
# # print(cat2.subject)

cat1 = Cat("英格兰短毛猫","小短毛")
# cat1.subject = "猫" # 类变量不允许使用对象名进行调用修改，只能通过类名修改
Cat.subject = "喵星人"
print(Cat.subject)
print(cat1.subject)


class Chinese:
    country = "中国"
    def __init__(self,id_num,name):
        self.id_num = id_num
        self.name = name