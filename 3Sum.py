# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# solution set must not contain duplicate triplets.


class Solution:
    def threesum(self, nums):
        nums.sort()
        res=[]

        for i in range(0,len(nums)):
            if nums[i] >0:
                break
            if i ==0 or nums[i] != nums[i-1]:
                self.threeSumZero(nums, i, res)
        return res

    def threeSumZero(self, nums, i, res):
        l = i+1
        h = len(nums)-1

        while(l<h):
            total = nums[i] + nums[l] + nums[h]
            if (total > 0):
                h = h-1
            elif (total <0):
                l = l+1
            else:
                res.append([nums[i], nums[l], nums[h]])
                l = l+1
                h = h-1
                while(l<h and nums[l] == nums[l-1]):
                    l = l+1
                while (l < h and nums[h] == nums[h -1]):
                    h = h - 1

s = Solution()
print(s.threesum([-1,0,1,2,-1,-4]))
print(s.threesum([0,1,1]))
