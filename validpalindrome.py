#Given a string s, return true if it is a palindrome, or false otherwise.
#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward.Alphanumeric characters include letters and numbers.

class Validpalindrome():
    def ispalindrome(self,s):
        r = len(s)-1
        l =0
        s=s.strip()
        s=s.lower()

        while(l<r):
            if(s[l].isalnum() and s[r].isalnum()):
                if(s[l]==s[r]):
                    l=l+1
                    r=r-1
                else:
                    return(False)
            if(not s[l].isalnum()):
                l=l+1
            if(not s[r].isalnum()):
                r=r-1
        return(True)

v = Validpalindrome()
print(v.ispalindrome('A man, a plan, a canal: Panama'))




