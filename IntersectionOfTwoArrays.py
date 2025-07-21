# 349. Intersection of Two Arrays
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.

class Solution:
    def intersection(self, nums1,nums2):

        # return list(set(nums1) & set(nums2))

        dict = {}
        res = []

        for i, num in enumerate(nums1):
            dict[num] = dict.get(num, 0) + 1

        for num in nums2:
            if num in dict:
                res.append(num)
                del dict[num]

        return res

s = Solution()
print(s. intersection([4,9,5],[9,4,9,8,4]))