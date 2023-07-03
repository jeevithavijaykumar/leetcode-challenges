#377. Combination Sum IV
#Given an array of distinct integers nums and a target integer target,
# return the number of possible combinations that add up to target.

class Combinationsum():
    def sumcombination(self,nums,target):
        dp={0:1}
        for i in range(1,target+1):
            dp[i]=0
            for n in nums:
                dp[i]=dp[i]+dp.get(i-n,0)
        return(dp[target])

c=Combinationsum()
print(c.sumcombination([1,2,3],4))