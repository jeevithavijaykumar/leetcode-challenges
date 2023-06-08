#35. Search Insert Position
#Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order. You must write an algorithm with O(log n) runtime complexity.
#Solution - use binary serach on sorted array - O(log n) complexity

class Sortedarray():
    def serachinsertosition(self,nums,target):
        l=0
        r=len(nums)-1
        while(l<=r):
            mid = (l+r)//2
            if(nums[mid]==target):
                return(mid)
            elif(target >nums[mid]):
                l = mid+1
            elif(target < nums[mid]):
                r=mid-1
        return(l)
    
s= Sortedarray()
print(s.serachinsertosition([1,3,5,6],7))
