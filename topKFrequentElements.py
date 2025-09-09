# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

from collections import Counter

class Solution:
    def topkfrequentelements(self, nums, k):

        freq = Counter(nums)

        freq_sorted = sorted(freq.items(), key=lambda x: x[1], reverse= True)

        return [num for num, _ in freq_sorted[:k]]


if __name__ == "__main__":
    s= Solution()
    result = s.topkfrequentelements([1,1,1,2,2,3],2)
    print(result)
    result = s.topkfrequentelements([1],1)
    print(result)