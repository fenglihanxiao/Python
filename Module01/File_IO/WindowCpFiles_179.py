"""
    1. 179_XXX -> copy files
"""
import os

################################################
# 1. Cp file version 1

# file1 = open("179.txt", "rb")
# file2 = open("179_2.txt", "wb")
#
#
# while True:
#     info = file1.read(1024)
#
#     if len(info) == 0:
#         break;
#     else:
#         file2.write(info)
#
# file1.close()
# file2.close()

################################################
# 1. Cp file version 2
# 2. 179.txt -> 179_copy.txt
# 3. Use slice technique to process the string

file_name1 = "10.194.102.154.txt"
idx = file_name1.rfind(".")
prefix = file_name1[0:idx]
postfix = file_name1[idx:]
file_name2 = prefix + "_copy" + postfix
print(file_name2)

file1 = open(file_name1, "rb")
file2 = open(file_name2, "wb")

while True:
    info = file1.read(1024)

    if len(info) == 0:
        break;
    else:
        file2.write(info)

file1.close()
file2.close()

################################################
# 1. os.path.exists

print(os.path.exists("10.194.102.154.txt"))
