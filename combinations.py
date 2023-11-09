#77. Combinations
#Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

class Solution():
    def combinations(self,n,k):
        res=[]

        def helperfn(start,comb):
            if(len(comb)==k):
                res.append(comb[:])
                return

            for j in range(start,n+1):
                comb.append(j)
                helperfn(j+1,comb)
                comb.pop()
        helperfn(1,[])
        return(res)

s=Solution()
print(s.combinations(4,2))