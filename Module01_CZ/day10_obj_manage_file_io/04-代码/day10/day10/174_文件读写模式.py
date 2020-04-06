"""
演示文件读写模式
"""
# with open("174.txt","w") as file :
#     file.write("hello python itcast2")

# with open("174-2.txt","a") as file :
#     file.write("--hello python itcast--")

# with open("174.txt","r") as file :
#     # file.write("hello python itcast2") # 不允许进行写操作
#     info = file.read()
#     print("读取到的信息是："+info)

# 复制文件
# readfile = open("174.txt","r")
# info = readfile.read()
# readfile.close()
#
# writefile = open("174-3.txt","w")
# writefile.write(info)
# writefile.close()

# readfile = open("壁纸.jpg","rb")
# info = readfile.read()
# readfile.close()
#
# writefile = open("壁纸-2.jpg","wb")
# writefile.write(info)
# writefile.close()

file2 = open("174-4.txt","w+")
file2.write("test info")
info = file2.read()
file2.close()

