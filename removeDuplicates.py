# Write a Python function that takes a list of numbers and returns  list with duplicates removed, while preserving the original order.

class Solution:

    def remove_duplicates(self,nums):
        seen = set()
        i=0

        while(i<len(nums)):
            if nums[i] in seen:
                nums.pop(i)
            else:
                seen.add(nums[i])
                i=i+1

        return nums

if __name__ == "__main__":
    s = Solution()
    print(s.remove_duplicates([3, 5, 2, 3, 2, 6, 5, 7]))

