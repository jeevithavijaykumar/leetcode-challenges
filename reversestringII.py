#541. Reverse String II
#Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string
#If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters,
#then reverse the first k characters and leave the other as original.

class String():
    def reversestring(self,s,k):
        s1=list(s)

        if(k==len(s)):
            return(s[::-1])
        for i in range(0,len(s1),2*k):
            s1[i:i+k]=s[i:i+k][::-1]

        return(''.join(str(e) for e in s1))

s=String()
print(s.reversestring('abcdefg',2))
print(s.reversestring('abcdefg',3))




