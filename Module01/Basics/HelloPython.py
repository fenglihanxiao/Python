# Practice debug statement
print("Hello Python")

a = 10
b = 5
c = a + b
print("Hello Python2")
print(c)
c = 99
print("Hello Python3:%d", c)
#####################################################

# ** operator has high precedences than *
print(2**3*4)
print(4*2**3)



def changeVal(x):
    x += 2;


#####################################################
def circleArea(r):
    pi = 3.14
    area = pi * r**2
    return area

x = 1
changeVal(x)
print(x)

r = 10
area = circleArea(r)
# print("Circle area=", area, " Second area", sep="|")
print("Circle area=%f" % area)

print ('1:\t|{0:>10},'.format('wangyu'))



