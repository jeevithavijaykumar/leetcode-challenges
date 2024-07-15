"""219. Contains Duplicate II"""
"""Given an integer array nums and an integer k,
Return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k."""

class Array():
    def containsDuplicate(self,nums,k):
        dict={}
        for i in range(0,len(nums)):
            if(nums[i] in dict and abs(i-dict[nums[i]])<=k):
                return(True)
            else:
                dict[nums[i]]=i
        return(False)