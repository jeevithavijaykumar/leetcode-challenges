#11. Container With Most Water
#You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the
# ith line are (i, 0) and (i, height[i]).
#Find two lines that together with the x-axis form a container, such that the container contains the most water.

class Container():
    def containerwithwater(self,height):
        res=0
        l=0
        r=len(height)-1
        while(l<r):
            area=(r-l)*(min(height[l],height[r]))
            res=max(res,area)
            if(height[l]<height[r]):
                l=l+1
            else:
                r=r-1
        return(res)

c=Container()
print(c.containerwithwater([1,8,6,2,5,4,8,3,7]))