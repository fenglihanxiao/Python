"""
演示单例模式
"""
class User:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(User)
        return cls.__instance

u1 = User()
u2 = User()
print(id(u1))
print(id(u2))

