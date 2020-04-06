"""
演示字典参数形参操作
"""
def test(**kwargs):
    print(kwargs)
    # **kwargs 将接收到的关键字参数按照参数传递的格式交给函数
    # {'a': 1, 'b': 2, 'c': 3}  —> a= 1,b = 2,c = 3
    # print(**kwargs)
    # *kwargs 对传递过来的所有字典参数中的键key进行显示操作
    # "a","b","c","d"
    print(*kwargs)
    print("aa","bb","cc")

# test(a= 1,b = 2,c = 3,d = 4)




# list1 = [1,2,3]
# tuple1 = {3,4,5}
# set1 = {5,6,7}
# dict1 = {"aa":123,"bb":456,"cc":789}
# str1 = "itcast"
#
# print(*str1)

def test2():
    # return 3,4,5 # 3,4,5->(3,4,5)
    # return [3,4,5]
    # return (3,4,5)
    return "itcast"

a,b,c,d,e,f = test2()
print(a)
print(b)
print(c)