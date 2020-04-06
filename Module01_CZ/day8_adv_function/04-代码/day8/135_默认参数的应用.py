"""
演示默认参数应用
"""
# str1 = "hello python"
# str1.index("???",0,len(str1))
# print(str1.index("o",6,12))

list1 = [1,2,3]
# list1.pop(len(list1)-1)
print(list1.pop(1), "list1=", list1)


# parameter 参数：形参
# arguments 参数：实参
def test(a,b=100):
    print(a, b)

test(1)