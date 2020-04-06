"""
    1. String encode
"""
str1 = "say goodbye"

dict1 = "".maketrans("abcdefg", "1234567")
print(dict1)
str2 = str1.translate(dict1)
print(str2)

"""
    1. String decode
"""
str3 = "s1y 7oo42y5"
dict2 = "".maketrans("1234567", "abcdefg")
str4 = str3.translate(dict2)
print(str4)