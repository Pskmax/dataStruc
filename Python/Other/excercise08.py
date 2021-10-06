<<<<<<< HEAD
def hbd(age):
    age = age/2
    if age == int(age):
        print('saimai is just 20, in base ',end='')
        return int(age)
    else:
        print('saimai is just 21, in base ',end='')
        return int(age)

if __name__ == '__main__':
    inp = int(input('Enter year : '))
=======
def hbd(age):
    age = age/2
    if age == int(age):
        print('saimai is just 20, in base ',end='')
        return int(age)
    else:
        print('saimai is just 21, in base ',end='')
        return int(age)

if __name__ == '__main__':
    inp = int(input('Enter year : '))
>>>>>>> 82f8b6dc910acd0c6b8055c749412f74ca69c302
    print(hbd(inp),end='!')