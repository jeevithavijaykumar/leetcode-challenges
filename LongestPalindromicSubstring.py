#Given a string s, return the longest palindromic substring in s
#A string is called a palindrome string if the reverse of that string is the same as the original string.

class Palindromicsubstring():
    def longestpalisubstring(self,s):
        res=''
        res_length = 0

        for i in range(0,len(s)):
            l=i
            r=i
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if(res_length < r-l+1):
                    res = s[l:r+1]
                    res_length = r-l+1
                l=l-1
                r=r+1
            l=i
            r=i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if(res_length < r-l+1):
                    res = s[l:r+1]
                    res_length = r-l+1
                l=l-1
                r=r+1

        return(res)

 a = Palindromicsubstring()
print(a.longestpalisubstring('cbbd'))


