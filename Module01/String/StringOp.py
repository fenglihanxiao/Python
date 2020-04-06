"""
    1. String basic operations
    2. Reference StringAPI.png
"""

str1 = "i have a family where have three amy people."
print(len(str1))
print(str1[5])
print(max(str1))
print(str1.index("amy"))
print("have" in str1)
print("feng" not in str1)
print(str1.islower())

"""
    1. String operation isXXX method
    2. Reference StringAPI.png
"""
str2 = "aaa"
print(str2.islower())

"""
    1. startswith and endswith
"""
str3 = "Feng"
print(str3.startswith("Fe"))

files = []
filename = "test.jpg"
filename2 = "test.png"
filename3 = "test.py"
files.append(filename)
files.append(filename2)
files.append(filename3)

for f in files:
    if f.endswith(".jpg") or f.endswith(".png"):
        print("Image files:%s" % f)
    else:
        print("The other type of file:%s" % f)