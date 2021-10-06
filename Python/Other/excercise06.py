'''
M=1000    CM=900    D=500    CD=400,
C=100    XC=90    L=50    XL=40,
X=10    IX=9    V=5    IV=4    I=1
'''
class translator:
    def decToRoman(self,num):
        dec = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        roman = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        newNum = ''
        i = 12
        while num > 0:
            for _ in range(num // dec[i]):
                newNum += roman[i]
                num -= dec[i]
            i -= 1
        return newNum
    def romanToDec(self,string):
        romanDict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        newNum = 0
        string = string.replace('IV','IIII').replace('IX','VIIII')
        string = string.replace('XL','XXXX').replace('XC','LXXXX')
        string = string.replace('CD','CCCC').replace('CM','DCCCC')

        for i in string:
            newNum += romanDict[i]
        return newNum


        

if __name__ == '__main__':
    inp = int(input('Enter number to translate : '))
    print(translator().decToRoman(inp))
    print(translator().romanToDec(translator().decToRoman(inp)))