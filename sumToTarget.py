# Write a function that finds all pairs of numbers in a list that sum to a target value.
# Return unique pairs (avoid duplicates like (1,5) and (5,1)).

class Solution:
    def sumToTarget(nums, target):

        seen =set()
        result = set()

        for i,num in enumerate(nums):
            complement = target -num
            if complement in seen:
                result.add(tuple(sorted((num,complement))))
            seen.add(num)

        return result

s = Solution
print(s.sumToTarget(nums=[1,2,3,4,5], target=7))