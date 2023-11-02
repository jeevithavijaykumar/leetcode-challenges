#152. Maximum Product Subarray
#Given an integer array nums, find a subarray that has the largest product, and return the product.

class Subarray():
    def maxproduct(self,nums):
        maxp = 1
        minp= 1
        res = max(nums)

        for n in nums:
            if(n==0):
                maxp = 1
                minp = 1
            temp = maxp*n
            maxp = max(temp, minp*n ,n)
            minp = min(temp,minp*n,n)
            res = max(res,maxp)
        return(res)

m = Subarray()
print(m.maxproduct([2,-3,2,-4,-5]))
print(m.maxproduct([-2,0,-1]))
