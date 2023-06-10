#Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

class Majorityelement():
    def findmajorityelement(self,nums):
        length = len(nums)
        majority=nums[0]
        count=1

        for i in range(1,length):
            if(majority==nums[i]):
                count=count+1
            else:
                count=count-1
                if(count==0):
                    majority=nums[i]
                    count=1
        return(majority)

m=Majorityelement()
nums=[1,2,1,3,1,1]
print(m.findmajorityelement(nums))

#solution 2 using hashmap

class Majorityelement():
    def findmajorityelement(self,nums):
        d={}
        for i in range(0,len(nums)):
            if(nums[i] not in d):
                d[nums[i]]=1
            else:
                d[nums[i]]=d[nums[i]]+1

        return(max(d,key=d.get))

m=Majorityelement()
nums=[1,2,1,3,1,1]
print(m.findmajorityelement(nums))



