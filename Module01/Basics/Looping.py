num = 1
sum = 0

while num <= 100:
    if num % 2 == 0:
        sum = sum + num
    num += 1

print("The sum=%d" % sum)

########################################################
num = 100
while num <= 999:
    if num % 35 == 0:
        sum += num
    num += 1

print("The sum=%d" % sum)

########################################################
# Palindrome for three digit
# num = 100
# while num <= 999:
#     bai_wei = num // 100
#     ge_wei = num % 10
#     if bai_wei == ge_wei:
#         #print("Palindrome=%d" % num)
#         print(num, end="-")
#     num += 1


cnt = 0
while True:
    for i in range(100):
        if i == 2:
            print("============ 1.")
            cnt += 1
            break
        i += 1
    if cnt == 2:
        break
    print("============ 2.")
print("================== 3.")