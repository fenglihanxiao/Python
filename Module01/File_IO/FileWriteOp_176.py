"""
    1. 176_XXX -> File write operations
"""

########################################################
# 1. Test for fd2.writelines(list1)

# fd1 = open("176.txt", "r")
# list1 = fd1.readlines()
# fd1.close()
#
# print(list1)
#
# fd2 = open("176_2.txt", "w")
# fd2.writelines(list1)
# fd2.close()

########################################################
# 1. Test for writing Chinese
fd3 = open("176_3.txt", "w")
fd3.write("窗前明月光\n")
fd3.write("疑是地上霜\n")
fd3.close()