#215. Kth Largest Element in an Array
#Given an integer array nums and an integer k, return the kth largest element in the array.

class Array():
    def kthlargest(self,nums,k):
        k=len(nums)-k

        def quickselect(l,r):
            p=l
            pivot=nums[r]
            for i in range(l,r):
                if(nums[i]<pivot):
                    nums[p],nums[i]=nums[i],nums[p]
                    p=p+1
            nums[r],nums[p]=nums[p],nums[r]
            if(k<p):
                return(quickselect(l,p-1))
            elif(k>p):
                return(quickselect(p+1,r))
            else:
                return(nums[p])
        return(quickselect(0,len(nums)-1))

k=Array()
print(k.kthlargest([3,2,3,1,2,4,5,5,6],4))
