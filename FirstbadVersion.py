#278. First Bad Version
#You are given an API bool isBadVersion(version) which returns whether version is bad.
# Implement a function to find the first bad version. You should minimize the number of calls to the API.
class Solution:
    def firstBadVersion(self, n):
        res=n
        l=1
        r=n
        while(l<r):
            mid=(l+r)//2
            if(self.isBadVersion(mid)):
                r=mid
                res=min(res,mid)
            else:
                l=mid+1
        return(res)

s=Solution()
print(s.firstBadVersion(6))
print(s.firstBadVersion(5))