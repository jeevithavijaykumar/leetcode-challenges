#90. Subsets II
#Given an integer array nums that may contain duplicates, return all possible subsets(the power set).
#The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution():
    def subsets(self,nums):
        nums.sort()
        res=[]

        def helperfn(i,subset):
            if(i==len(nums)):
                res.append(subset[::])
                return
            subset.append(nums[i])
            helperfn(i+1,subset)
            subset.pop()
            while(i+1<len(nums) and nums[i+1]==nums[i]):
                i=i+1
            helperfn(i+1,subset)

        helperfn(0,[])
        return(res)

s=Solution()
print(s.subsets([1,2,2,3]))

