"""
演示多继承
"""
class Father:
    def sing(self):
        print("擅长唱歌")
    def dance(self):
        print("跳舞很难看")
class Mother:
    def sing(self):
        print("唱歌很难听")
    def dance(self):
        print("擅长跳舞")

class Child(Father,Mother):
    def sing(self):
        print("儿子不会唱歌")
        Father.sing(self)
        Mother.sing(self)
        super().sing()

c = Child()
c.sing()
# c.dance()

# (<class '__main__.Child'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>)
print(Child.__mro__)