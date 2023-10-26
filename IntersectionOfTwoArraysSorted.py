#350. Intersection of Two Arrays II
#Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays
# and you may return the result in any order.
#What if the given array is already sorted? How would you optimize your algorithm?

class Array():
    def intersectionofarrays(self,nums1,nums2):
        a=sorted(nums1)
        b=sorted(nums2)
        i=0
        j=0
        res=[]

        while(i<len(a) and j<len(b)):
            if (a[i] < b[j]):
                i = i + 1
            elif (a[i] > b[j]):
                j = j + 1
            else:
                res.append(a[i])
                i = i + 1
                j = j + 1
        return (res)
a=Array()
print(a.intersectionofarrays([4,9,5],[9,4,9,8,4]))

s = "dog cat cat dog"
a= s.split()
print(a)
