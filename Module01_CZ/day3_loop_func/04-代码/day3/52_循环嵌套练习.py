"""
打印
*
**
***
****
*****
"""
# 分析
# 1.每一行是由不同的*组成的，要循环着打印
# 2.一共有多行，打印多少行需要使用循环来控制

j = 1
while j <= 5 :
    i = 1
    while i <= j :
        print("*" , end = "")
        i += 1
    print()
    j += 1