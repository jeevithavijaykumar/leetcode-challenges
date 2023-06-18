#205. Isomorphic Strings
#Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#Input: s = "egg", t = "add" .   Output: true

class Isomorphicstrings():
    def isomorphic(self,s,t):
        mapst={}
        mapts={}

        for i in range(0,len(s)):
            c1=s[i]
            c2=t[i]
            if((c1 in mapst and mapst[c1]!=c2)or(c2 in mapts and mapts[c2]!=c1)):
                return(False)
            mapst[c1]=c2
            mapts[c2]=c1

        return(True)

i = Isomorphicstrings()
print(i.isomorphic('egg','ard'))