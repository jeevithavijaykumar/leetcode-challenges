#Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result.
# Return k after placing the final result in the first k slots of nums.

class Removeduplicatefromsortedarray():
    def removeduplicates(self,nums):
        k = 1

        for i in range(1, len(nums)):
            if (nums[i] != nums[i - 1]):
                nums[k] = nums[i]
                k = k + 1
        return (k)

r = Removeduplicatefromsortedarray()
nums=[1,1,1,1,2,3,4,4,5]
print(r.removeduplicates(nums))

