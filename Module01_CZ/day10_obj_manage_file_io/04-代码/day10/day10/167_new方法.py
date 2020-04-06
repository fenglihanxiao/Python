"""
演示__new__方法
"""
class User:
    def __new__(cls, *args, **kwargs):
        print("user new method is running----------------")
        # 创建对象由object完成
        instance = object.__new__(User)
        return instance

    def __init__(self,name,age):
        print("user init method is running...")
        self.name = name
        self.age = age

user1 = User("张三", 18)

