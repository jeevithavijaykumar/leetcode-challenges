#You are given an integer array nums. You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.
#Return true if you can reach the last index, or false otherwise

class Jumpgame():
    def canjump(self,nums):
        goal=len(nums)-1

        for i in range(len(nums)-2,-1,-1):
            if(i+nums[i]>=goal):
                goal=i
        if(goal==0):
            return(True)
        else:
            return(False)
j=Jumpgame()
print(j.canjump([2,3,1,1,4]))

