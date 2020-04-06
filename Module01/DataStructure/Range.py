###########################################
# 1. not include 5
r1 = range(1, 5)
print(list(r1))

###########################################
# 1. not include 10
# 2. 2 is step
r2 = range(1, 10, 2)
print(list(r2))

###########################################
# 1. Same effect with range
i = 0
while i < 5:
    print("Hello")
    i += 1

print("=================================")
for i in range(5):
    print("Hello")

print("=================================")
###########################################
# 1. Prefer use _ to note is a place holder for iteration variable
###########################################
for _ in range(5):
    print("Hello")