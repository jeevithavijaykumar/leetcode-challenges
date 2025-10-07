# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

class Solution:

    def twoSum(self,numbers, target):

        l = 0
        r = len(numbers)-1

        while( l<r):
            if (numbers[l]+ numbers[r] == target):
                return [l+1, r+1]
            elif( numbers[l]+ numbers[r] < target):
                l = l+1
            else:
                r = r-1
        return [-1, -1]

s = Solution()
print(s.twoSum([2,3,4], 6))
print(s.twoSum([-1,0], -1))