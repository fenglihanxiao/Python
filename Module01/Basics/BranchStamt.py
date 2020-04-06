#############################################################
# IF statements
a = 10
b = 15

if a < b and True:
    print("a < b")
    print("hello=", a, "hell", sep='|')

num = 102
if num > 100:
    print("Num=", num, " Large than 100")

if num % 2 == 0:
    print("num %d is even number" % num)

# Print 3 digit and even number
# 1. Large than 99 and less than 1000
# 2. num % 2 == 0

num2 = 191

if num2 > 99 and num2 < 1000 and num2 % 2 == 0:
    print("Bingo num=", num2)

#############################################################
# if else statements
# num3 = 11
# num4 = 18
# if num3 > num4 :
#     print("Large number1 is:%d" % num3)
# else:
#     print("Large number2 is:%d" % num4)
#
# num2 = int(input("Please enter a number:"))
# if num2 % 2 == 0:
#     print("Number %d is even number" % num2)
# else:
#     print("Number %d is odd number" % num2)

#############################################################
# if elif and else statements
score = 92
if score == 100:
    print("Full score, go buy a bicycle")
elif score >= 95 and score < 100:
    print("Go to happy land")
elif score >= 90 and score < 95:
    print("Get a new toy")
elif score > 85 and score < 90:
    print("still live")
else:
    print("As kicked")

#############################################################
# Nested if statements
x = 0
if x >= 0:
    if x % 2 == 0:
        print("%d is even num." % x)
    else:
        print("%d is odd num." % x)
else:
    print("%d is negative num." % x)
