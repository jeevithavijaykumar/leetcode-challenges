""" 367 - Valid Perfect square
Given a positive integer num, return true if num is a perfect square or false otherwise."""

class Solution():
    def isPerfectSquare(self,n):
        l=0
        r=n
        while(l<=r):
            mid = (l+r)//2
            if(mid*mid==n):
                return(True)
            elif(mid*mid>n):
                r=mid-1
            else:
                l=mid+1
        return(False)

s=Solution()
print(s.isPerfectSquare(14))
