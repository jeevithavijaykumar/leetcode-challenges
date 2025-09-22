# Given a string s and a substring sub, return the number of times sub occurs in s.
# Substrings can overlap if needed.

class Solution:
    def count_substring(self, s, sub):
        count =0
        start = 0

        while True:
            idx = s.find(sub, start)
            if idx ==-1:
                break
            count = count+1
            start = idx+1

        return count

s = Solution()
print(s.count_substring('abababa','aba'))
print(s.count_substring('hello world','o'))




from collections import Counter

def mostfrequentchar(s):
    map = Counter(s)
    max_count = max(map.values())
    res=[]

    for k,v in map.items():
        if (v==max_count):
            res.append(k)

    return sorted(res)[0]

m = mostfrequentchar("abbccc")
n = mostfrequentchar('aabb')
print(m)
print(n)


def mostfrequentchar(s):
    map = Counter(s)
    max_val = max(map.values())
    res =[]

    for k,v in map.items():
        if(v==max_val):
            res.append(k)

    return min(res)

m = mostfrequentchar("abbccc")
n = mostfrequentchar('aabb')
print(m)
print(n)



def mostfrequentchar(s):

    return min([k for k,v in Counter(s).items() if v == max(Counter(s).values())])

s = mostfrequentchar('abbccc')
print(s)
n = mostfrequentchar('aabb')
print(n)


def secondLargestNum(nums):

    num_set = set(nums)
    if(len(num_set)<2):
        return None

    num_set_sorted = sorted(num_set, reverse=True)
    return num_set_sorted[1]

s = secondLargestNum([4, 1, 7, 7, 3])
print(s)


def secondLargestNum(nums):
    first = second = float('-inf')

    for n in set(nums):
        if (n > first):
            second = first
            first = n
        elif(first > n > second):
            second = n
    return second if second != float('-inf') else None

s = secondLargestNum([4, 1, 7, 7, 3])
print(s)





def removeduplicates(nums):
    seen = set()
    res =[]

    for num in nums:
        if num not in seen:
            res.append(num)
            seen.add(num)
    return res

r = removeduplicates([4, 1, 7, 4, 3, 1, 7])
print(r)




def maxSumSubarray(nums,k):
    res = float('-inf')
    curr_sum = sum[:k]

    for i in range(k,len(nums)):
         curr_sum = curr_sum + num[i] - nums[i-k]
         res = max(res, curr_sum)

    return res

m = maxSumSubarray([2, 1, 5, 1, 3, 2], 3)
print(m)





def longestSubarrayK(nums, k):
    max_len =0
    curr_sum = 0
    left = 0

    for right in range(0,len(nums)):
        curr_sum = curr_sum + nums[right]

        while( curr_sum > k):
            curr_sum = curr_sum - nums[left]
            left = left+1

        max_len = max(max_len, right-left+1)

    return max_len

print(longestSubarrayK([1,2,3,4,5],7))






























