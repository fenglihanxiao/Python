class Cat:
    @classmethod
    def speak(cls):
        print("猫叫")

def show():
    print("hello module")

module = [1,2,3]
age = 18

# print(__name__) # __main__  # module_193

# 对测试代码进行访问控制，如果是当前类访问运行，否则不运行
if __name__ == "__main__":
    # 测试
    print("hello 测试")
    print(len(module))
