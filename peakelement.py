#162. Find Peak Element
#A peak element is an element that is strictly greater than its neighbors.
#Given a 0-indexed integer array nums, find a peak element, and return its index.
# If the array contains multiple peaks, return the index to any of the peaks.

class Peakelement():
    def ispeak(self,nums):
        l=0
        r=len(nums)-1

        while(l<r):
            mid=(l+r)//2
            if(nums[mid]<nums[mid+1]):
                l=mid+1
            else:
                r=mid
        return(l)

p=Peakelement()
print(p.ispeak([1,2,3,1]))