#283. Move Zeroes
#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#Note that you must do this in-place without making a copy of the array.
#Input: nums = [0,1,0,3,12]      Output: [1,3,12,0,0]

class Movezeros():
    def movezerostotheend(self,nums):
        l=0
        for r in range(0,len(nums)):
            if(nums[r]):
                nums[l],nums[r]=nums[r],nums[l]
                l=l+1
        return(nums)
m=Movezeros()
nums=[0,2,0,0,6,9,0,8,4]
print(m.movezerostotheend(nums))

