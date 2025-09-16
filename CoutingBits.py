# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

class Solution:
    def countBits(self, n):
        res = [0] * (n+1)

        for i in range(0,n+1):
            res[i] = (i&1) + res[i >> 1]

        return res

s= Solution()
print(s.countBits(5))



