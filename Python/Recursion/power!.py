def power(a, b):
    if b == 0:
        return 1
    else:
        return a*power(a, b-1)

if __name__ == '__main__':
    inp = input('Enter Input a b : ').split(' ')
    a = int(inp[0])
    b = int(inp[1])
    print(power(a,b))