#You are given two integer arrays nums1 and nums2,sorted in non-decreasing orde
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#Merge nums1 and nums2 into a single array sorted in non-decreasing order.The final sorted array should not be returned by the function,
# but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n,
# where the first m elements denote the elements that should be merged,and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

class Mergedarray():
    def mergearray(self,nums1,nums2,m,n):
        r = len(nums1) - 1
        p = m - 1
        q = n - 1
        while (p >= 0 and q >= 0):
            if (nums1[p] < nums2[q]):
                nums1[r] = nums2[q]
                r = r - 1
                q = q - 1
            else:
                nums1[r] = nums1[p]
                p = p - 1
                r = r - 1
        while (q >= 0):
            nums1[r] = nums2[q]
            q = q - 1
            r = r - 1

m= Mergedarray()
nums1 = [2,2,3,0,0,0]
nums2 = [1,5,6]
m.mergearray(nums1,nums2,3,3)
print(nums1)

