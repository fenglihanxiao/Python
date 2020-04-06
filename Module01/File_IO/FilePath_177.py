"""
    1. 177_XXX： —> File path (relative path and absolute path)
"""

########################################################
# 1. Test for absolute file path

# fd = open("E:\\FengLi_Files\\Python\\Works\\Module01\\File_IO\\177.txt", "w")
# or use / directly
# fd = open("E:/FengLi_Files/Python/Works/Module01/File_IO/177_01.txt", "w")
# fd.write("Test for python ...\n")
# fd.close()

########################################################
# 1. Test for relative file path
fd = open("../Basics/177_1.txt", "w")
fd.write("Test for python ...\n")
fd.close()