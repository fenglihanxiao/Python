"""
演示数据存储结构嵌套
"""
# list1 = [1,2,3]
# list2 = [4,5,6,7]
# list3 = ["itcast","黑马程序员"]
# tuple1 = (5,4,3)
# set1 = {8,7,6}
# list4 = [list1,list2,list3,tuple1,set1]
# # print(list4)
# for a in list4:
#     # 取出的数据仍然是列表，还需要循环
#     for data in a:
#         print(data)
#     print("----------------")

list1 = [[1,2],[3,4],(5,6),{7,8},9]
for a in list1:
    # 如果是可迭代的东西，执行循环，否则执行打印
    if isinstance(a,list) or isinstance(a,set) or isinstance(a,tuple):
        # 取出的数据仍然是列表，还需要循环
        for data in a:
            print(data)
    else:
        print(a)
    print("----------------")

# print(isinstance(123,list))