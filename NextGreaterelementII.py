#503. Next Greater Element II
#Given a circular integer array nums, return the next greater number for every element in nums.
class List():
    def nextGreaterElements(self, nums):
        if (not nums):
            return ([])
        stack = []
        greatest = max(nums)
        res = [-1] * len(nums)

        for i in list(range(0, len(nums)))*2:
            while (stack and nums[stack[-1]] < nums[i]):
                res[stack.pop()] = nums[i]
            stack.append(i)
        return (res)

l=List()
print(l.nextGreaterElements([5,4,3,2,1]))

