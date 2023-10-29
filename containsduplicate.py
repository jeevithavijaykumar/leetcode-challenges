#217. Contains Duplicate
#Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

class Containsduplicate():
    def duplicate(self,nums):
        dictionary={}

        for i in range(0,len(nums)):
            if(nums[i] in dictionary):
                return (True)
            else:
                dictionary[nums[i]] =i
        return(False)
c=Containsduplicate()
nums=[1,2,3,1]
print(c.duplicate(nums))