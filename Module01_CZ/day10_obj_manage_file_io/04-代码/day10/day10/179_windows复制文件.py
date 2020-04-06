"""
案例：windows复制文件
分析：
1. 整体文件复制采用 rb wb模式进行
2. 复制文件需要更改名称，变化是有规则的
3. 1.txt -> 1 - 副本.txt
"""
# 版本一：
# file1 = open("d:/1.txt","rb")
# file2 = open("d:/2.txt","wb")
#
# while True:
#     info = file1.read(1024)
#     if len(info) == 0:
#         break
#     else:
#         file2.write(info)
#
# file1.close()
# file2.close()


# 版本二：

# 1.txt -> 1 - 副本.txt
# file1_name = "d:/1.txt"
# idx = file1_name.rfind(".")
# # print(file1_name[0:idx])
# # print(file1_name[idx:])
# file2_name = file1_name[0:idx]+ " - 副本" + file1_name[idx:]
# 
# file1 = open(file1_name,"rb")
# file2 = open(file2_name,"wb")
# 
# while True:
#     info = file1.read(1024)
#     if len(info) == 0:
#         break
#     else:
#         file2.write(info)
# 
# file1.close()
# file2.close()

import os
print(os.path.exists("d:/3.txt"))