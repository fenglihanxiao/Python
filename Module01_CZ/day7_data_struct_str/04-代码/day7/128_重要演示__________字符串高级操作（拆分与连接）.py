"""
案例：将以下个人信息组织成一个对象
	“name:张三   age:18”
"""
# 对象对应的类模型
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return "姓名：%s，年龄：%d" % (self.name,self.age)
# 包含个人信息的字符串
info = "name:张三 age:18"

# 对信息进行处理后，创建的Person对象使用处理后信息中的数据



























"""
infos = info.split(" ")             # ["name:张三","age:18"]

info_name = infos[0].split(":")     # ["name","张三"]
info_age = infos[1].split(":")      # ["age","18"]

p = Person(info_name[1],int(info_age[1]))
print(p)
"""