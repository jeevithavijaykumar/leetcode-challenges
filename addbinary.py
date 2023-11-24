#67 Add Binary
#Given two binary strings a and b, return their sum as a binary string.

class Binaryadd():
    def binaryaddition(self,a,b):
        res=[]
        carry=0
        c1 = len(a)-1
        c2 = len(b)-1

        while(c1>=0 or c2>=0):
            if(c1>=0):
                x1 = ord(a[c1])-ord('0')
            else:
                x1=0
            if(c2>=0):
                x2 = ord(b[c2])-ord('0')
            else:
                x2=0
            sum=(x1+x2+carry)%2
            if((x1+x2+carry)>1):
                carry=1
            else:
                carry=0
            res.append(sum)
            c1=c1-1
            c2=c2-1
        if(carry):
            res.append(carry)
        return(''.join(str(i) for i in res[::-1]))

b= Binaryadd()
print(b.binaryaddition("1010","1011"))


