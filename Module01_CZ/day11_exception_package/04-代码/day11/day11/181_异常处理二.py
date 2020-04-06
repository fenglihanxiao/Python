"""
演示异常处理方案二
"""
# print("读文件")
# try:
#     f = open("1.txt","r")
#     # f.write("呵呵")
# except:
#     print("读取文件失败")
# finally:
#     f.close()
#     print("finally...")
# print("读文件结束")

print("读文件")
try:
    f = open("1.txt","r")
    f.write("呵呵")
finally:
    f.close()
    print("finally...")
print("读文件结束")