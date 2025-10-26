#561. Array Partition
#Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn)
# such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

class Arraypartition():
    def maxsuminarray(self,nums):
        nums.sort()
        maxsum=0

        for i in range(0,len(nums),2):
            maxsum=maxsum+nums[i]
        return(maxsum)
        
a= Arraypartition()
print(a.maxsuminarray([6,2,6,5,1,2]))
