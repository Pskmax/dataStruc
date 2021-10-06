print('*** multiplication or sum ***')
inp1, inp2 = input('Enter num1 num2 : ').split()
inp1 = int(inp1)
inp2 = int(inp2)
if inp1*inp2 > 1000:
    print('The result is', inp1+inp2)
else:
    print('The result is', inp1*inp2)