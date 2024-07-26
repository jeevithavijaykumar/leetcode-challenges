""" 38. Count and Say """
""" Given a positive integer n, return the nth element of the count-and-say sequence. """
"""Example 1:  Input: n = 4  Output: "1211"
# Explanation:
countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
# countAndSay(4) = RLE of "21" = "1211" 
"""

class Solution():
    def countAndSay(self,n):
        if(n==1):
            return('1')
        else:
            prev = self.countAndSay(n-1)
            result=""
            count=1

            for i in range(len(prev)):
                if(i<len(prev)-1):
                    if(prev[i]==prev[i+1]):
                        count+=1
                    else:
                        result += str(count)+prev[i]
                        count=1
                else:
                    result+=str(count)+prev[i]
            return(result)

s=Solution()
print(s.countAndSay(4))

