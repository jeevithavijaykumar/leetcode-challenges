#Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

class Solution:
    def subArraySum(self,nums,k):
        prefix_sum = {0:1}
        curr_sum =0
        count =0

        for num in nums:
            curr_sum = curr_sum + num
            count = count + prefix_sum.get(curr_sum-k,0)
            prefix_sum[curr_sum] = 1 + prefix_sum.get(curr_sum,0)

        return count

s= Solution()
print(s.subArraySum([1,1,1], 2))
print(s.subArraySum([1,2,3], 3))




def longestSubstring(s):
    seen ={}
    start = 0
    max_len = 0

    for i, ch in enumerate(s):
        if(ch in seen and seen[ch] >= start):
            start = seen[ch] +1

        seen[ch] = i
        max_len = max(max_len, i-start+1)
    return max_len

s= longestSubstring('bbbbb')
print(s)
j= longestSubstring('pwwkew')
print(j)




def longest_subarray_sum_k(nums,k):
    prefix_sum ={0:-1}
    curr_sum  = 0
    max_len = 0

    for i,num in enumerate(nums):
        curr_sum = curr_sum+num
        if(curr_sum-k in prefix_sum):
            max_len = max(max_len, i-prefix_sum[curr_sum-k])
        if curr_sum not in prefix_sum:
            prefix_sum[curr_sum] =i

    return max_len




def longestSubarray(nums,k):
    prefix_sum = {0:-1}
    max_len = 0
    curr_sum = 0

    for i,num in enumerate(nums):
        curr_sum = curr_sum + num
        if(curr_sum -k in prefix_sum):
            max_len = max(max_len, i - prefix_sum[curr_sum-k])
        if(curr_sum not in prefix_sum):
            prefix_sum[curr_sum] = i

    return max_len

l = longestSubarray([1, -1, 5, -2, 3], 3)
print(l)





import pandas as pd

def compute_mean_large_csv(filename, column_name, chunk_size = 100_000):

    total_sum =0
    total_count = 0

    for chunk in pd.read_csv(filename, chunksize=chunk_size):
        chunk_col = chunk[column_name].dropna()
        total_sum = total_sum + chunk_col.sum()
        total_count = total_count + chunk_col.count()

    return total_sum/total_count if total_count> 0 else None

c = compute_mean_large_csv('hardware_readings.csv' 'temeparture')
print('Mean Temperature: ', c)



def compute_mean(filename, column_name, chunk_size = 100000):
    total_sum = 0
    total_count =0

    for chunk in pd.read_csv(filename, chunksize=chunk_size):




