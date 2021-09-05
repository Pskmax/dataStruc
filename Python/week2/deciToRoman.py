import math
class translator:
    def deciToRoman(self, num):
        dec = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        roman = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']

        s = ''
        i = 12
        while num > 0:
            for _ in range(num // dec[i]):
                s += roman[i]
                num -= dec[i]
            i -= 1
        return s
    def romanToDeci(self, s):
        romansDict = {
                "I" : 1,
                "V" : 5,
                "X" : 10,
                "L" : 50,
                "C" : 100,
                "D" : 500,
                "M" : 1000
            }
        num = 0
        s = s.replace("IV","IIII").replace("IX","VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            num += romansDict[char]
        return num


num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))
print(translator().romanToDeci(translator().deciToRoman(num)))