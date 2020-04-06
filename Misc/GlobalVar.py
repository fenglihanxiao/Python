nums = [11, 22]

def test():
    global nums
    nums += [33, 44]


print(nums)

test()

print(nums)
