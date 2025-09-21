# You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within the inclusive range.
# A number x is considered missing if x is in the range [lower, upper] and x is not in nums.
# Return the shortest sorted list of ranges that exactly covers all the missing numbers.
# That is, no element of nums is included in any of the ranges, and each missing number is covered by one of the ranges.

class Solution:
    def findMissingRanges(self, nums, lower,upper):
        prev = lower -1
        res =[]

        nums.append(upper+1)

        for curr in nums:
            if((curr-prev) >1 ):
                res.append([prev+1, curr-1])
            prev = curr

        return res

s= Solution()
print(s.findMissingRanges([0,1,3,50,75], 0, 99))
print(s.findMissingRanges([-1], -1, -1))