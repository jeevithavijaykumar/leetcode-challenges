# 33. Search in Rotated Sorted Array
# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.

class Solution:
    def search(self, nums, target):

        left =0
        right= len(nums)-1

        while(left<=right):
            mid = (left+right)//2

            if(target==nums[mid]):
                return(mid)

            # Check if left half is sorted
            if(nums[left] <= nums[mid]):
                if(nums[left]<=target<nums[mid]):
                    right = mid-1
                else:
                    left=mid+1
            # if right half is sorted
            else:
                if(nums[mid]<target<=nums[right]):
                    left = mid+1
                else:
                    right = mid-1

        return(-1)

s= Solution()
print(s.search([4,5,6,7,0,1,2],0))
print(s.search([4,5,6,7,0,1,2],3))