"""
演示函数实参为不可变类型与可变类型的区别
"""
# def test(a,b): # a->@m->@100   最终 a->@100
#     a = 1   # a->变化->@1
#     b = 2
#
# m = 100 # m->@100
# n = 200
# print(m)
# print(n)
# print("---------------")
# test(m,n)
# print(m) # 此时m->??? @100
# print(n)


def test(a):    # a->list1->@9999  最终 a->@9999
    a.append("itcast") # a对地址中的数据进行了操作 a->变化？没有->@9999

list1 = ["hello","python"]  # list1->@9999
print(list1)
print("--------------")
test(list1)
print(list1) # 输出list1,输出list1的指向->@9999













