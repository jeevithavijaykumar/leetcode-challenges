#39. Combination Sum
#Given an array of distinct integers candidates and a target integer target,
#Return a list of all unique combinations of candidates where the chosen numbers sum to target.
#The same number may be chosen from candidates an unlimited number of times.

class Integers():
    def combinationsum(self,candidates,target):
        res=[]

        def dfs(i,cur,total):
            if(total==target):
                res.append(cur.copy())
                return
            if(i>=len(candidates) or total>target):
                return
            cur.append(candidates[i])
            dfs(i,cur,total+candidates[i])
            cur.pop()
            dfs(i+1,cur,total)

        dfs(0,[],0)
        return(res)

i=Integers()
print(i.combinationsum([2,3,5],8))
