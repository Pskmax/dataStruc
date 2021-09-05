print("*** multiplication or sum ***")
x,y = input("Enter num1 num2 : ").split()
x = int(x)
y = int(y)
multi = x*y
sum = x+y
if multi > 1000:
    print("The result is",sum)
else:
    print("The result is",multi)
