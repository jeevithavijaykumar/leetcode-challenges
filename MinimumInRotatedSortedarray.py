#153. Find Minimum in Rotated Sorted Array
#Given the sorted rotated array nums of unique elements, return the minimum element of this array.

class Rotatedsortedarray():
    def findmin(self,nums):
        l=0
        r=len(nums)-1

        while(l<r):
            if(nums[l]<nums[r]):
                return(nums[l])
            mid = (l+r)//2
            if(nums[mid]>=nums[l]):
                l=mid+1
            else:
                r=mid
        return(nums[l])

r = Rotatedsortedarray()
print(r.findmin([4,5,6,7,0,1,2]))
print(r.findmin([3,4,5,1,2]))