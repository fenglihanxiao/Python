price = float(input("Please enter your total price = "))
member = input("Are you a member, please enter y or n = ")

if price >= 100:
    price -= 50
elif price >= 50:
    price -= 30
elif price >= 30:
    price -= 10
else:
    price = price

if member == "y":
    price *= 0.8

print("Your final price=%.2f" % price)


