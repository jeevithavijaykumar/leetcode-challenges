#215. Kth Largest Element in an Array
#Given an integer array nums and an integer k, return the kth largest element in the array.
#Note that it is the kth largest element in the sorted order, not the kth distinct element.

class Array():
    def kthlargest(self,nums,k):
        k=len(nums)-k

        def quickselect(l,r):
            p=l
            pivot=nums[r]
            for i in range(l,r):
                if(nums[i]<=pivot):
                    nums[i],nums[p]=nums[p],nums[i]
                    p=p+1
            nums[p],nums[r]=nums[r],nums[p]
            if(p>k):
                return quickselect(l,p-1)
            elif(p<k):
                return quickselect(p+1,r)
            else:
                return(nums[p])
        return quickselect(0,len(nums)-1)

k=Array()
print(k.kthlargest([3,2,3,1,2,4,5,5,6],4))
