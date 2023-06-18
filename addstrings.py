#415. Add Strings
#Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
#You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
# You must also not convert the inputs to integers directly

class Addstrings():
    def stringsaddition(self,num1,num2):
        c1=len(num1)-1
        c2=len(num2)-1
        carry=0
        res=[]

        while(c1>=0 or c2>=0):
            if(c1>=0):
                x1=ord(num1[c1]) - ord('0')
            else:
                x1=0
            if(c2>=0):
                x2=ord(num2[c2]) - ord('0')
            else:
                x2=0
            sum=(x1+x2+carry)%10
            carry=(x1+x2+carry)//10
            res.append(sum)
            c1=c1-1
            c2=c2-1
            print(x1)
            print(x2)
            print(sum)
            print(carry)
            print(res)
        if(carry):
            res.append(carry)
        return ''.join(str(i) for i in res[::-1])

a=Addstrings()
num1='11'
num2='123'
print(a.stringsaddition(num1,num2))
