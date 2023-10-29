#Given a collection of candidate numbers (candidates) and a target number (target),
#find all unique combinations in candidates where the candidate numbers sum to target.
#Each number in candidates may only be used once in the combination.

class Array():
    def combinationsum(self,candidates,target):
        res=[]
        candidates.sort()

        def dfs(cur,pos,total):
            if(total==target):
                res.append(cur.copy())
            if(total>target):
                return
            prev=-1
            for i in range(pos,len(candidates)):
                if(prev==candidates[i]):
                    continue
                cur.append(candidates[i])
                dfs(cur,i+1,total+candidates[i])
                cur.pop()
                prev=candidates[i]
        dfs([],0,0)
        return(res)

c=Array()
print(c.combinationsum([10,1,2,7,6,1,5],8))