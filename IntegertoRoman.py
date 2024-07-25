""" 12. Integer to Roman """
"""Given an integer, convert it to a Roman numeral."""

class Solution():
    def integerToRoman(self,num):
        dict={'M':1000,'CM':900,'D':500,'CD':400,'C':100,'L':50,'XL':40,'X':10,'V':5,'IV':4,'I':1}

        result=''
        for key, value in dict.items():
            while(num>=value):
                result+=key
                num-=value
        return(result)

s=Solution()
print(s.integerToRoman(1998))