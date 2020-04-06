"""
    1. String find operations
    2. String rfind operations
"""
str1 = "hello itcast hello"
print(str1.find("itcast"))
print(str1.rfind("itcast"))

print(str1.find("t"))
print(str1.rfind("t"))

# Return -1 if substr is not found
idx = str1.find("feng")
print(idx)
# Raises ValueError when the substring is not found.
# idx2 = str1.index("feng")

"""
    1. String replace operations
    2. String rfind operations
"""
str2 = str1.replace("hello", "hi")
print("str1=%s" % str1)
print("str2=%s" % str2)

str2 = str1.replace("hello", "hi", count=1)
print("str1=%s" % str1)
print("str2=%s" % str2)