""" 31. Next Permutation """
""" Given an array of integers nums, find the next permutation of nums.
The replacement must be in place and use only constant extra memory. """

class Solution():
    def nextPermutation(self,nums):
        if(len(nums)<2):
            return

        pivot=-1
        for i in range(len(nums)-2,-1,-1):
            if(nums[i]<nums[i+1]):
                pivot=i
                break
        if(pivot==-1):
            nums.reverse()
            return
        for j in range(len(nums)-1,pivot,-1):
            if(nums[j]>nums[pivot]):
                nums[j],nums[pivot]= nums[pivot],nums[j]
                break
        nums[pivot+1:] = nums[pivot+1:][::-1]

s=Solution()
s.nextPermutation([1,1,5])
s.nextPermutation([3,2,1])

