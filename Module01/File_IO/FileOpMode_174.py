"""
    1. 174_XXX: File operation mode
"""

########################################
# 1. with Append mode
# with open("174.txt", "a") as fd1:
#     fd1.write("Hello")


########################################
# 1. with read mode

# with open("174.txt", "rb") as fd1:
#     info = fd1.read()
#     print("Read content:" + str(info))

###################################################################
# # 1. Read one file content and write to a new file with char
#
# file_read = open("174.txt", "r")
# info = file_read.read()
# file_read.close()
#
# file_write = open("174_cp.txt", "w")
# file_write.write(info)
# file_write.close()


###################################################################
# 1. Read one file content and write to a new file with BINARY mode
# 2. "rb" and "wb" are compatible with text process and binary process
# file_read = open("FileIOMode1.png", "rb")
# info = file_read.read()
# file_read.close()
#
# file_write = open("FileIOMode1_cp.png", "wb")
# file_write.write(info)
# file_write.close()

###################################################################
# 1. File mode in both write and read mode by post append "+"

file_wr = open("174.txt", "w+")
file_wr.write("hello python")
info = file_wr.read()
print("File write and read info:" + info)
file_wr.close()
