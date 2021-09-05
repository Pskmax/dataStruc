def hbd(age):
    ### Enter Your Code Here ###
    x = age/2
    if x == int(x):
        print("saimai is just 20, in base ",end='')
        return int(x)
    else:
        print("saimai is just 21, in base ",end='')
        return int(x)


year = input("Enter year : ")
print(hbd(int(year)),end='!')