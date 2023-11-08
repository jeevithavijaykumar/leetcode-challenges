#53. Maximum Subarray
#Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Maxsubarray():
    def maxsubarray(self,nums):
        maxsum=nums[0]
        sum=0

        for i in range(0,len(nums)):
            if(sum<0):
                sum=0
            sum=sum+nums[i]
            maxsum=max(maxsum,sum)
        return(maxsum)

m=Maxsubarray()
print(m.maxsubarray([-2,1,-3,4,-1,2,1,-5,4]))
