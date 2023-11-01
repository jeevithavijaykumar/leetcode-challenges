#209. Minimum Size Subarray Sum
#Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
#whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

class MinimumSubarray():
    def minsubarray(self,nums,target):
        if(sum(nums)<target):
            return(0)
        i=0
        j=0
        cursum=0
        minlen=len(nums)

        while(j<len(nums) and i<=j):
            cursum=cursum+nums[j]
            if(cursum>=target):
                minlen=min(minlen,j-i+1)
                cursum=cursum-nums[i]-nums[j]
                i=i+1
            else:
                j=j+1
        return(minlen)

m=MinimumSubarray()
print(m.minsubarray([2,3,1,2,4,3],7))