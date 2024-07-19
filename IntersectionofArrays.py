"""Given two integer arrays nums1 and nums2, return an array of their intersection
Each element in the result must be unique and you may return the result in any order """

class Solution():
    def intersection(self,nums1,nums2):
        a=set(nums1)
        b=set(nums2)
        return(list(a & b))

s=Solution()
print(s.intersection([1, 2, 2, 1], [2, 2]))
