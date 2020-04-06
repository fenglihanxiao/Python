dict1 = {"name": "Feng", "age": 18}
#######################################
#   1. If key does not exist then insert
dict1["name2"] = "Stephanie"
print(dict1)

#######################################
#   1. get return None, it is a preferred way
val = dict1.get("name2_")
if val != None:
    print(val)
else:
    print("No exist!")

print(dict1["name2"])

#######################################
#   1.
print(dict1.keys())
print(dict1.values())
print(dict1.items())

"""
https://blog.csdn.net/spynao/article/details/50176761
"""
k={}
s = [('Tom', 5), ('Jone', 2), ('Susan', 4), ('Tom', 4), ('Tom', 1)]

for item in s:
    print("%s:%d" % (item[0], item[1]))



# for i,j in s:
#     # 注意不能写成 if not k[i],因为其返回值不是None,而是error
#     if i not in k.keys():
#         l=[]
#         l.append(j)
#         k[i]=l
#     else:
#         k[i].append(j)
#
# print(k)

#######################################################
# 10-数据存储.docx
dict1 = {"name":"itcast","age":11}
# v = dict1.popitem()
# print(v)
# v = dict1.popitem()
# print(v)
val = dict1.items()
print(val)