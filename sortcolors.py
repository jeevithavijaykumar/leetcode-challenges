#75. Sort Colors
#Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color
# are adjacent,with the colors in the order red, white, and blue.
#We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#You must solve this problem without using the library's sort function.

class Sortcolors():
    def sorting(self,nums):
        l=0
        r=len(nums)-1
        i=0
        while(i<=r):
            if(nums[i]==0):
                nums[l],nums[i]=nums[i],nums[l]
                l=l+1
                i=i+1
            elif(nums[i]==2):
                nums[r],nums[i]=nums[i],nums[r]
                r=r-1
            else:
                i=i+1
        return(nums)
s=Sortcolors()
print(s.sorting([2,0,2,1,1,0]))