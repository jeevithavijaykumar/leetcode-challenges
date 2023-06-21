#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#Notice that the solution set must not contain duplicate triplets.

class Threesum():
    def threesumarr(self,nums):
        nums.sort()
        res=[]
        for i in range(0,len(nums)):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            l=i+1
            r=len(nums)-1
            while(l<r):
                threesum = nums[i]+nums[l]+nums[r]
                if(threesum<0):
                    l=l+1
                elif(threesum>0):
                    r=r-1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l=l+1
                    while(l<r and nums[l]==nums[l-1]):
                        l=l+1
        return(res)
t=Threesum()
print(t.threesumarr([-1,0,1,2,-1,-4]))