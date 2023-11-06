#560. Subarray Sum Equals K
#Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
#A subarray is a contiguous non-empty sequence of elements within an array.

class Subarray():
    def subarraysum(self,nums,k):
        prefixsum={0:1}
        cursum=0
        count=0

        for i in range(0,len(nums)):
            cursum=cursum+nums[i]
            count=count+prefixsum.get(cursum-k,0)
            prefixsum[cursum]=1+prefixsum.get(cursum,0)
        return(count)
s=Subarray()
print(s.subarraysum([1,1,1],2))
