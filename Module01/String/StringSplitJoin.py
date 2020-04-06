"""
    1. String partition
    2. String rpartition
"""
str1 = "hello my family, we will do better"
print(str1.partition("my"))
print(str1.rpartition("e"))

"""
    1. String split
    2. String splitline
    3. string join
"""
str1 = "hello itcast python"
print(str1.split("t"))

str2 = "hello, feng,itcast, python"
print(str2.split(","))


str1 = "hello\nitcast\npython"
print(str1)
print(str1.splitlines())

str1 = "*"
str1 = str1.join("itcast")
print(str1)

"""
    1. str1ing +
    2. has to be concatenate with str type by using str(type)
 
"""
str1 = "Feng love "
str2 = "Stephanie"
num = 88.88
strd = str(num)
str3 = str1 + str2 + " " + strd
print(str3)