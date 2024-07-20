"""342 Power of four
Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x."""

import math
class Solution():
    def poweroffour(self,n):
        if(n<0 or n==0):
            return(False)
        if(n==1):
            return(True)
        sqrtn = math.sqrt(n)
        x = math.log2(sqrtn)
        return(int(x)==x)

s= Solution()
print(s.poweroffour(n=16))


