class Solution:
    def longestPalindrome(self,s: str) -> str:
        if s == "" or len(s) == 1:
            return s
        palindromeLengths = {}
        n = len(s)

        a = 0
        b = n-1

        while a < n and b >= 0:
            if checkPalindrome(s,a,b, palindromeLengths):
                return s[a:b+1]

            if b == n-1:
                b = (b-a) - 1
                a = 0
            else:
                a += 1
                b += 1
        return "error"


def checkPalindrome(s,x,y, palindromeLengths):
    index = getIndex(x,y)
    a,b=getAB(index)
    # print(s,index,palindromeLengths)
    if s == "" or len(s) == 1: return True
    if index in palindromeLengths:
        return (x,y) == palindromeLengths[index]

    while a >= 0 and b < len(s):
        if s[a] != s[b]:
            if a != b and a != b + 1:
                palindromeLengths[index] = (a+1,b-1)
            return False
        a -= 1
        b += 1
    palindromeLengths[index] = (a+1,b-1)
    return True

def getAB(index):
    if index % 2 == 0:
        a = int(index / 2)
        b = a
    else:
        a = int(index/2)
        b = a + 1
    return (a,b)

def getIndex(a,b):
    return a + b

