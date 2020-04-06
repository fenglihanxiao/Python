"""
演示引用类型参数
"""
class Person:
   """定义人类，具有name和age两个变量"""
   def __init__(self,name,age):
       self.name = name
       self.age = age

name1 = "大帅"
age1 = 18
p1 = Person("小帅",17)

def demo(name,age,person):
    # 修改name,age,person对应的值（在函数内部修改）
    name = "大帅哥"
    age = 28
    person.name = "小帅哥"
    person.age = 27

print(name1)
print(age1)
print(p1.name)
print(p1.age)
print("--------------------")
demo(name1,age1,p1)
print(name1)
print(age1)
print(p1.name)
print(p1.age)
