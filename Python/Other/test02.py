<<<<<<< HEAD
def factor_list(num):
    out = list()
    for i in range(1, num):
        if num % i == 0:
            out.append(i)
    return out


if __name__ == '__main__':
    print(' *** Perfect Number Verification ***')
    number = int(input('Enter number : '))
    if number < 0:
        print('Only positive number !!!')
        quit()
    else:
        lst = factor_list(number)
        if sum(lst) == number:
            print(f'{number} is a PERFECT NUMBER.')
        else:
            print(f'{number} is NOT a perfect number.')
=======
def factor_list(num):
    out = list()
    for i in range(1, num):
        if num % i == 0:
            out.append(i)
    return out


if __name__ == '__main__':
    print(' *** Perfect Number Verification ***')
    number = int(input('Enter number : '))
    if number < 0:
        print('Only positive number !!!')
        quit()
    else:
        lst = factor_list(number)
        if sum(lst) == number:
            print(f'{number} is a PERFECT NUMBER.')
        else:
            print(f'{number} is NOT a perfect number.')
>>>>>>> 82f8b6dc910acd0c6b8055c749412f74ca69c302
        print('Factors :', lst)