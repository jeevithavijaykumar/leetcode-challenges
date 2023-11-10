#205. Isomorphic Strings
#Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#Input: s = "egg", t = "add" .   Output: true

class Isomorphicstrings():
    def isomorphic(self,s,t):
        d1={}
        d2={}

        if(len(s)!=len(t)):
            return(False)

        for i in range(0,len(s)):
            if((s[i] in d1 and d1[s[i]]!=t[i])or(t[i] in d2 and d2[t[i]]!=s[i])):
                return(False)
            d1[s[i]]=t[i]
            d2[t[i]]=s[i]

        return(True)

i = Isomorphicstrings()
print(i.isomorphic('egg','ard'))