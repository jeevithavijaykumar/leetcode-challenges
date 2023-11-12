#704. Binary Search
#Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.

class Array():
    def Binarysearch(self,nums,target):
        l=0
        r=len(nums)-1
        while(l<=r):
            mid=(l+r)//2
            if(nums[mid]==target):
                return(mid)
            elif(nums[mid]<target):
                l=mid+1
            elif(nums[mid]>target):
                r=mid-1
        return(-1)

a=Array()
print(a.Binarysearch([-1,0,3,5,9,12],9))
print(a.Binarysearch([-1,0,3,5,9,12],2))
