#229. Majority Element II
#Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

class Majority():
    def majorityelement(self,nums):
        d={}
        res = []
        maj = len(nums)//3

        for i in range(0,len(nums)):
            if(nums[i] not in d):
                d[nums[i]]=1
            else:
                d[nums[i]]=d[nums[i]]+1
            if(d[nums[i]] > maj and nums[i] not in res):
                res.append(nums[i])
        return(res)

m=Majority()
nums=[1,2,2,2,3,1,1]
print(m.majorityelement(nums))
