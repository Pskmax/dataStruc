class MyInt:
    def __init__(self, data) -> None:
        self.data = data
        
    def isPrime(self):
        if self.data > 1:
            for i in range(2, self.data+1):
                if (self.data % i) != 0:
                    return str(self.data) + ' isPrime : True'
                elif self.data == 2:
                    return str(self.data) + ' isPrime : True'
                else:
                    return str(self.data) + ' isPrime : False'
       
    def showPrime(self):
        num = ''
        for i in range(2,self.data + 1):
            if i > 1:
                for j in range(2, i):
                    if (i % j) == 0:
                        break
                else:
                    num += str(i) + ' '
        return 'Prime number between 2 and ' + str(self.data) + ' : ' + str(num)

    def __sub__(self, other):
        a = self.data
        b = (other.data)/2
        return int(a-b)

if __name__ == '__main__':
    print(' *** class MyInt ***')
    a,b = input('Enter 2 number : ').split()
    a = int(a)
    b = int(b)
    a = MyInt(a)

    b = MyInt(b)

    print(a.isPrime())

    print(b.isPrime())

    print(a.showPrime())

    print(b.showPrime())

    print(a-b)
