# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchRange(self,nums, target):

        def searchPosition(nums,target, is_left_search):

            l=0
            r= len(nums)-1
            idx =-1

            while(l <= r):
                mid = (l+r)//2

                if nums[mid] > target :
                    r = mid-1
                elif nums[mid] < target:
                    l = mid+1
                else:
                    idx = mid
                    if is_left_search:
                        r = mid-1
                    else:
                        l =mid+1

            return idx

        first = searchPosition(nums, target, 1)
        last = searchPosition(nums, target, 0)

        print ([first,last])


s= Solution()
s.searchRange([5,7,7,8,8,10], 8)
s.searchRange([5,7,7,8,8,10], 6)







