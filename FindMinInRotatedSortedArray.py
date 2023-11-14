#153. Find Minimum in Rotaed Sorted Array
#Array on length n with unique elements,sorted in ascending order is rotated betweeen 1 and n times
#Return the minimum element of this array

class Array():
    def findminimum(self,nums):
        l=0
        r=len(nums)-1

        while(l<r):
            if(nums[l]<nums[r]):
                return(nums[l])
            mid=(l+r)//2
            if(nums[mid]<nums[l]):
                r=mid
            else:
                l=mid+1
        return(nums[l])

a=Array()
print(a.findminimum([3,4,5,1,2]))
