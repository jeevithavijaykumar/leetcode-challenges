#350. Intersection of Two Arrays II
#Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each elementin the result must appear as many times as it shows in both arrays
# and you may return the result in any order.

import collections
class Array():
    def intersectionofarrays(self,nums1,nums2):
        c = collections.Counter(nums1)
        res=[]

        for i in range(0,len(nums2)):
            if(c[nums2[i]] >0):
                res.append(nums2[i])
                c[nums2[i]]=c[nums2[i]]-1
        return(res)
a=Array()
print(a.intersectionofarrays([4,9,5],[9,4,9,8,4]))


#Solution2 - Using dictionary
class Arrays():
    def intersectionoftwoarrays(self,nums1,nums2):
        res = []
        d = {}
        for i in range(0, len(nums1)):
            d[nums1[i]] = 1 + d.get(nums1[i], 0)

        for j in range(0, len(nums2)):
            if (d.get(nums2[j],0) >0):
                res.append(nums2[j])
            d[nums2[j]] = d[nums2[j]] - 1
        return (res)
a=Array()
print(a.intersectionofarrays([4,9,5,6],[9,4,9,8,4,6,8]))

