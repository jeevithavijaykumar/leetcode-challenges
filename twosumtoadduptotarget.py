#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Solution : check for target - element1 = element2 , if element2 is in array return that element.To do so, we use dictionary

class Twosum():
    def twosumtotarget(self,nums,target):
        dic ={}
        for i,num in enumerate(nums):
            next_number = target-nums[i]
            if next_number in dic :
                return(dic[next_number],i)
            else:
                dic[num]=i

t =Twosum()
nums=[1,2,3,7]
print(t.twosumtotarget(nums,9))




