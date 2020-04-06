"""
演示文件基本操作
"""
# # 格式一
# # 1.打开文件
# file = open("1.txt","w")
# # 2.操作文件
# file.write("hello itcast python")
# # 3.关闭文件
# file.close()

# 格式二
with open("2.txt","w") as file2 :
    file2.write("hello python itcast")