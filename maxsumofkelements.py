#Given an array of integers of size ‘n’, calculate the maximum sum of ‘k’ consecutive elements in the array.

import sys

class Array():
    def maxsumofk(self,nums,k):
        maxsum = -sys.maxsize-1

        for i in range(0,len(nums)-k+1):
            cur_sum=0
            for j in range(0,k):
                cur_sum = cur_sum + nums[i+j]
            maxsum = max(maxsum,cur_sum)

        return(maxsum)
    
a=Array()
print(a.maxsumofk([1,4,2,10,2,3,1,0,20],4))