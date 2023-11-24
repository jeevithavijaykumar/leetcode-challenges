#387. First Unique Character in a String
#Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class String():
    def fisrtuniquecharacter(self,s):
        d={}

        for i in range(0,len(s)):
            d[s[i]]=1+d.get(s[i],0)
        for j in range(0,len(s)):
            if(d[s[j]]==1):
                return(j)
        return(-1)

s=String()
print(s.fisrtuniquecharacter('leetcode'))
print(s.fisrtuniquecharacter('aabb'))