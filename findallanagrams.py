#438 Find All Anagrams in a string
#Given two strings s and p, return an array of all the start indices of p's anagrams in s.
#You may return the answer in any order.
class String():
    def findanagrams(self,s,p):

        if(len(p)>len(s)):
            return([])
        res=[]
        pcount={}
        scount={}

        for i in range(0,len(p)):
            pcount[p[i]]=1+pcount.get(p[i],0)
            scount[s[i]]=1+scount.get(s[i],0)
        if(pcount==scount):
            res.append(0)

        l=0
        for r in range(len(p),len(s)):
            scount[s[r]]=1+scount.get(s[r],0)
            scount[s[l]]=scount[s[l]]-1
            if(scount[s[l]]==0):
                scount.pop(s[l])
            l=l+1
            if(scount==pcount):
                res.append(l)

        return(res)

s=String()
print(s.findanagrams('cbaebabacd','abc'))
print(s.findanagrams('abab','ab'))
