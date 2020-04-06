"""
    1. Else execute after for iteration and else is part of for loop
    2. Only not execute in condition of break
"""
for data in range(5):
    print(data)
else:
    print("Post operation after for loop")

print()

for data in range(5):
    if data == 3:
        break
    print(data)
else:
    print("Post operation after for loop")

print("==============================================")

# count = 0
# while count < 5:
#    print (count, " 小于 5")
#    count = count + 1
# else:
#    print (count, " 大于或等于 5")