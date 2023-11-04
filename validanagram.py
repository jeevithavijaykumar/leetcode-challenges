#242. Valid Anagram
#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
#typically using all the original letters exactly once.

class Anagram():
    def isanagram(self,s,t):

        if(len(s)!=len(t)):
            return(False)
        
        ds = {}
        dt = {}
        for i in range(0,len(s)):
            ds[s[i]] = 1 + ds.get(s[i],0)
            dt[t[i]] = 1 + dt.get(t[i],0)

        for j in ds:
            if(ds[j] != dt.get(j,0)):
                return(False)
        return(True)

a=Anagram()
print(a.isanagram("anagram","nagaram"))