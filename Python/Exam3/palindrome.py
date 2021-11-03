def isPalindrome(s):
    newS = ''.join(filter(str.isalpha,s))
    newS = newS.lower()
    if len(newS) < 2:
        return True
    if newS[0] != newS[-1:]:
        return False
    return isPalindrome(newS[1:-1])
    
inp = input('Enter Input : ')
if isPalindrome(inp):
    print("'"+inp+"'","is palindrome")
else:
    print("'"+inp+"'","is not palindrome")