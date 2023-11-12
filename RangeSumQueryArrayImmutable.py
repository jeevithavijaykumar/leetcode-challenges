#Given an integer array nums, handle multiple queries of the following type:
#Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
#Implement the NumArray class:
#NumArray(int[] nums) Initializes the object with the integer array nums.int sumRange(int left, int right)
# Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right])

class Rangesumquery():
    def __init__(self,nums):
        self.nums=nums
        length = len(nums)
        prefix_arr = [0]*(length+1)
        for i in range(0,length):
            prefix_arr[i+1]= prefix_arr[i]+nums[i]
        self.prefix_arr = prefix_arr

    def sumcal(self,left,right):
        result=0
        result = self.prefix_arr[right+1]-self.prefix_arr[left]
        return(result)

nums = [-2, 0, 3, -5, 2, -1]
r = Rangesumquery(nums)
print(r.sumcal(0,2))
print(r.sumcal(2,5))
print(r.sumcal(0,5))