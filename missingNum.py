#Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array

class Solution:
    def missingNumber(self,nums):

        n = len(nums)
        expected_sum = n*(n+1)//2
        actual_sum = sum(nums)

        return expected_sum-actual_sum

s= Solution()
print(s.missingNumber([9,6,4,2,3,5,7,0,1]))