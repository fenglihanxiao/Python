"""
    1. 175_XXX -> File read operation
"""


########################################
# 1. First solution to read a large file
# 2. Adopt for read()

# fd = open("175.txt", "r")
# while True:
#     # For reading a large file, we use 1024 (1K)
#     info = fd.read(1024)
#     print(info)
#
#     if len(info) <= 0:
#         break
# fd.close()

########################################
# 1. Second solution to read a large file
# 2. Adopt for readline()

# fd = open("175.txt", "r")
# while True:
#     # For reading a large file, we use 1024 (1K)
#     info = fd.readline()
#     print(info, end="|")
#
#     if len(info) <= 0:
#         break
# fd.close()

########################################
# 1. Third solution to read a large file
# 2. Adopt for readlines()

fd = open("175.txt", "r")
info = fd.readlines()
print(info)
fd.close()