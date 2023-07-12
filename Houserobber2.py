#213. House Robber II
#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
# All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile,
# adjacent houses have a security system connected,
# and it will automatically contact the police if two adjacent houses were broken into on the same night.

class HouseRobber():
    def houserob(self,nums):

        def helperfn(num):
            rob1=0
            rob2=0
            for n in num:
                temp=max(rob1+n,rob2)
                rob1=rob2
                rob2=temp
            return(rob2)

        r1=helperfn(nums[:len(nums)-1])
        r2=helperfn(nums[1:])
        return(max(r1,r2,nums[0]))

h=HouseRobber()
print(h.houserob([1,2,3]))

