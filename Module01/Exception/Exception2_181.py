"""
    181_XXX -> finally
"""
#################################################################
# 1. try, except and finally
try:
    file1 = open("181.txt", "r")
    file1.write("test")

except:
    print("Exception occurs here ...")
finally:
    ##############################################################
    # 1. regular path and exception pass all go to here to process
    # 2 It does resources clean, e.g, file close, socket close
    #    and memory clean up here
    print("finally statements occur here ...")
    file1.close()


#################################################################
# 2. try and finally
# try:
#     file1 = open("181.txt", "w+")
#     file1.write("test")
# finally:
#     ##############################################################
#     # 1. regular path and exception pass all go to here to process
#     # 2 It does resources clean, e.g, file close, socket close
#     #    and memory clean up here
#     print("finally statements occur here ...")
#     file1.close()

