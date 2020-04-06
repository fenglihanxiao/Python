"""
1. 173_XXX -> Basic file operation
"""
##########################################
# 1. Need explicitly close the file
# fd = open("test.txt", "w")
# fd.write("Hello python world")
# fd.close()

##########################################
# 1. Do not need close the file
with open("2.txt", "w") as file2:
    file2.write("Hello Stephanie, please be a nice baby!")

