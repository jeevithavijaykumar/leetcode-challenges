# Given a positive integer n, write a function that returns the number of set bits in its binary representation

class Solution:
    def hammingweight(self,n):

        count = 0
        while n:
            count = count + (n&1)
            n = n>>1
        return count

h = Solution()
print(h. hammingweight(11))
print(h. hammingweight(128))
print(h. hammingweight(2147483645))