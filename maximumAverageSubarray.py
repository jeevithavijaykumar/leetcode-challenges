# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
# Any answer with a calculation error less than 10-5 will be accepted.


class Solution:
    def findMaxAvgSubarray(self, nums, k):
        curr_sum = sum(nums[:k])
        max_avg = curr_sum/k

        for i in range(k, len(nums)):
            curr_sum = curr_sum + nums[i] - nums[i-k]
            max_avg = max(max_avg, curr_sum/k)

        return round(max_avg, 2)

s= Solution()
print(s.findMaxAvgSubarray([1, 12, -5, -6, 50, 3], 4))

