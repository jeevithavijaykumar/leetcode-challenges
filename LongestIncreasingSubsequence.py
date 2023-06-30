#300. Longest Increasing Subsequence
#Given an integer array nums, return the length of the longest strictly increasing subsequence

class LongestincreasingSubsequence():
    def LIScal(self,nums):
        LIS=[1]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if(nums[j]>nums[i]):
                    LIS[i]=max(LIS[i],1+LIS[j])
        return(max(LIS))

l=LongestincreasingSubsequence()
print(l.LIScal([10,9,2,5,3,7,101,18]))