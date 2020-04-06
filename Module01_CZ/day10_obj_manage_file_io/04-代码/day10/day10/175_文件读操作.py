"""
演示文件读操作
"""
# file = open("175.txt","r")
# while True:
#     info = file.read(1024) 
#     print(info ,end="")
#     # 如果读取到了最后，停止循环
#     if len(info) == 0:
#         break
# file.close()

# file = open("175.txt","r")
# while True:
#     info = file.readline()
#     print(info)
#     if len(info) == 0:
#         break
# file.close()

file = open("175-2.txt","r")
result = file.readlines()
print(result)
file.close()


