#Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
#Return the sum of the three integers.

class Solution():
    def threesumclosest(self,nums,target):
        nums.sort()
        res=sum(nums[:3])

        for i in range(0,len(nums)-2):
            l=i+1
            r=len(nums)-1
            while(l<r):
                total=nums[i]+nums[l]+nums[r]
                if(abs(total-target)<abs(res-target)):
                    res=total
                if(total<target):
                    l=l+1
                else:
                    r=r-1
        return(res)


s=Solution()
print(s.threesumclosest([-1,2,1,-4],1))
