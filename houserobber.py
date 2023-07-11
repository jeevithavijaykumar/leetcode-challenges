#198. House Robber
#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
# it will automatically contact the police if two adjacent houses were broken into on the same night.

class Houserobber():
    def robber(self,nums):
        rob1=0
        rob2=0
        for n in nums:
            temp=max(rob1+n,rob2)
            rob1=rob2
            rob2=temp
        return(rob2)

h=Houserobber()
print(h.robber([2,7,9,3,1]))
