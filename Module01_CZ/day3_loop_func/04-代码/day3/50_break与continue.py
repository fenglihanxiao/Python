"""
演示break与continue
break:终止循环
continue:提前结束本轮循环
"""
#演示break功能
# i = 1
# while i <= 10:
#     # 如果查到了5，结束循环
#     if i == 5 :
#         break
#     print("查数:%d" % i)
#     i += 1
# print("结束")



#演示continue功能
i = 0
while i < 10:
    i += 1
    # 如果碰到5，则直接跳过，查下面的数字
    if i % 2 == 0 :
        continue
    print("查数:%d" % i)
print("结束")

