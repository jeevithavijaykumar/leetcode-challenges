# Given an array of positive integers nums and an integer K,
# Find the length of the longest contiguous subarray whose sum is less than or equal to K.


class Solution:
    def longestSubarrarySum(self, nums, k):
        maxlen = 0
        left =0
        curr_sum =0

        for right in range(0,len(nums)):
            curr_sum = curr_sum + nums[right]

            while(curr_sum > k):
                curr_sum = curr_sum - nums[left]
                left = left +1

            maxlen = max(maxlen, right-left+1)

        return maxlen

s = Solution()
print(s.longestSubarrarySum([1,2,3,4,5],7))