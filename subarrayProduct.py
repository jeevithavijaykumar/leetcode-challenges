# Given an array of integers nums and an integer k,
# return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.


class Solution:
    def subarrayProduct(self, nums,k):
        if(k<=1):
            return 0

        left=0
        product=0
        count=0

        for right,num in enumerate(nums):
            product = product*num
            while(product >= k):
                product = product//num
                left = left+1
            count = count + (right - left +1)

        return count

s = Solution()
print(s.subarrayProduct([10,5,2,6], 100))