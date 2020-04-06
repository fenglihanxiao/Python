def foo():
    print("abc")
    print("def")


def sumEvenNum(x):
    # Function comments definition
    """ Sum even number"""
    num = 1
    sum = 0

    while num <= x:
        if num % 2 == 0:
            sum = sum + num
        num += 1
    return sum


def max2(x, y):
    if x > y:
        return x
    else:
        return y


def max3(a, b, c):
    x = max2(a, b)
    y = max2(x, c)
    return y


def multiple():
    return 3, 4, 5


foo()
print("======================================")
# Control point function name
sum = sumEvenNum(1000)
print("The sum=%d" % sum)

val = max2(89, 72)
print("Max=%d" % val)

val = max2(12.1, 54.76)
print("Max=%.4f" % val)

# Even max2 return value, we still can use function call without a receiver
print(max2("abc", "ABC"))

# Get multiple return values
x, y, z = multiple()
print(x, y, z)

val_max = max3(9, 12, 17)
print(val_max)