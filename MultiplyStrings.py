""" 43 Multiply strings"""
""" Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly."""

class Solution():
    def multiply(self,num1,num2):

        if(num1=="0" or num2=="0"):
            return("0")

        l1= len(num1)
        l2=len(num2)
        result = [0]*(l1+l2)
        num1=num1[::-1]
        num2=num2[::-1]
        for i in range(l1):
            for j in range(l2):
                mul = (ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0'))
                result[i+j]+=mul
                result[i+j+1]+=result[i+j]//10 # carry calculation
                result[i+j]=result[i+j]%10 #updating the result after carry calculation

        while(len(result)>1 and result[-1]==0):
            result.pop()
        # reverse the result list and convert it into a string
        return("".join(str(i) for i in result[::-1]))

s= Solution()
print(s.multiply("123","456"))




