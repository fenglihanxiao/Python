j = 1
while j <=5:
    i = 1
    while i <= 5:
        print("*", end="")
        i += 1
    print()
    j += 1

print("=========================================")

# outer variable to control inner loop variable
j = 1
while j <=5:
    i = 1
    # Pay attention i <= j
    while i <= j:
        print("*", end="")
        i += 1
    print()
    j += 1

print("=========================================")
i = 1
j = 1

while j <= 9:
    i = 1
    while i <= j:
        print("%d*%d=%d" % (i, j, i * j), end="\t")
        i += 1
    print()
    j += 1