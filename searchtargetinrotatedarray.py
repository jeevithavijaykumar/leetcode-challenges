#33. Search in Rotated Sorted Array
#There is an integer array nums sorted in ascending order (with distinct values).
#Given the array nums after the possible rotation and an integer target,
#Return the index of target if it is in nums, or -1 if it is not in nums.

class Targetposition():
    def targetinrotatedarray(self,nums,target):
        l=0
        r=len(nums)-1

        while(l<=r):
            mid=(l+r)//2
            if(nums[mid]==target):
                return(mid)
            if(nums[l]<=nums[mid]):
                if(target>nums[mid] or target<nums[l]):
                    l=mid+1
                else:
                    r=mid-1
            else:
                if(target<nums[mid] or target>nums[r]):
                    r=mid-1
                else:
                    l=mid+1
        return(-1)

t=Targetposition()
print(t.targetinrotatedarray([4,5,6,7,0,1,2],6))



#approach 2
class Targetposition():
    def targetinrotatedarray(self,nums,target):
        l =0
        r =len(nums)-1

        while (l<=r):
            if (nums[l]<target):
                if (nums[r]<nums[l] and nums[r]!=target):
                    l=l+1
                elif (nums[r]==target):
                    return(r)
                else:
                    r=r-1
            elif (nums[l]> target):
                if (nums[r]<nums[l] and nums[r]!=target):
                    r=r-1
                elif (nums[r]==target):
                    return(r)
                else:
                    l=l +1
            else:
                return(l)
        return(-1)
t=Targetposition()
print(t.targetinrotatedarray([4,5,6,7,0,1,2],6))



