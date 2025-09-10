# Given an array of strings words and an integer k, return the k most frequent strings.
# Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.


from collections import Counter

class Solution:
    def topkfrequentwords(self, nums, k):

        freq = Counter(nums)

        freq_sorted = sorted(freq.items(), key=lambda x: (-x[1],x[0]))

        return [num for num, _ in freq_sorted[:k]]


if __name__ == "__main__":
    s= Solution()
    result = s.topkfrequentwords(["the","day","is","sunny","the","the","the","sunny","is","is"],4)
    print(result)