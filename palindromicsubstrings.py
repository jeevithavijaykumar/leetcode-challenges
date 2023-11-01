#647. Palindromic Substrings
#Given a string s, return the number of palindromic substrings in it.

class Palindromicsubstr():
    def countsubstr(self,s):
        res = 0
        for i in range(0, len(s)):
            l=i
            r=i
            while (l>=0 and r<len(s) and s[l]==s[r]):
                res =res+1
                l=l-1
                r=r+1
            l=i
            r=i+1
            while (l>=0 and r<len(s) and s[l]==s[r]):
                res = res + 1
                l=l-1
                r=r+1
        return(res)

p=Palindromicsubstr()
print(p.countsubstr("aaa"))

