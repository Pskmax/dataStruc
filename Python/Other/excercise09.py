<<<<<<< HEAD
def bon(w):
    charDict = {
        "a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8,
        "i" : 9, "j" : "10" , "k" : 11, "l": 12, "m" : 13, "n" : 14, "o": 15, "p" : 16,
        "q" : 17, "r" : 18, "s" : 19 , "t" : 20, "u" : 21, "v" : 22, "w" : 23 , "x" : 24,
        "y" : 25, "z" : 26
    }
    w = list(w)
    maxWord = max(w,key=w.count)
    return charDict[maxWord] * 4

if __name__ == '__main__':
    secretCode = input("Enter secret code : ")
=======
def bon(w):
    charDict = {
        "a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8,
        "i" : 9, "j" : "10" , "k" : 11, "l": 12, "m" : 13, "n" : 14, "o": 15, "p" : 16,
        "q" : 17, "r" : 18, "s" : 19 , "t" : 20, "u" : 21, "v" : 22, "w" : 23 , "x" : 24,
        "y" : 25, "z" : 26
    }
    w = list(w)
    maxWord = max(w,key=w.count)
    return charDict[maxWord] * 4

if __name__ == '__main__':
    secretCode = input("Enter secret code : ")
>>>>>>> 82f8b6dc910acd0c6b8055c749412f74ca69c302
    print(bon(secretCode))