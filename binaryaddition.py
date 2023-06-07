class Addbinary():
    def binaryaddition(self,a:str,b:str):
        i = len(a)-1
        j=len(b)-1
        res= ""
        carry=0

        while(i>=0 or j>=0):
            sum =carry
            if(i>=0):
                sum+= ord(a[i])-ord('0')
            if(j>=0):
                sum+=ord(b[j])-ord('0')
            i=i-1
            j=j-1
            if(sum>1):
                carry=1
            else:
                carry=0
            res+=str(sum%2)
        if(carry!=0):
            res+=str(carry)
        return(res[::-1])

a=Addbinary()
print(a.binaryaddition('11','1'))
