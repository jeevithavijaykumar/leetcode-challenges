#1221. Split a String in Balanced Strings
#Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
# Given a balanced string s, split it into some number of substrings such that:Each substring is balanced.
#Return the maximum number of balanced strings you can obtain.

class Balancedstring():
    def balancedstr(self,s):
        balancedstrcnt=0
        count=0
        for i in range(0,len(s)):
            if(s[i]=='R'):
                count+=1
            elif(s[i]=='L'):
                count-=1
            if(count==0):
                balancedstrcnt+=1
        return(balancedstrcnt)

b=Balancedstring()
print(b.balancedstr('RLRRLLRLRL'))