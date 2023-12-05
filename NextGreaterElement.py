#496. Next Greater Element I
#Given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
#find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2.
# If there is no next greater element, then the answer for this query is -1.

class List():
    def nextGreaterElement(self, nums1,nums2):
        a = {}
        stack = []

        for i in range(0, len(nums2)):
            while (stack and stack[-1] < nums2[i]):
                a[stack.pop()] = nums2[i]
            stack.append(nums2[i])

        res = []
        for j in range(0, len(nums1)):
            res.append(a.get(nums1[j],-1))
        return (res)

l=List()
print(l.nextGreaterElement([4,1,2],[1,3,4,2]))
print(l.nextGreaterElement([2,4],[1,2,3,4]))