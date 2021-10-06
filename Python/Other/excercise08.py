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
    print(hbd(inp),end='!')