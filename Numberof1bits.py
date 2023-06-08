#Write a function that takes the binary representation of an unsigned integer and
# returns the number of '1' bits it has (also known as the Hamming weight).

class hammingWeight():
    def numofones(self,n):
        count=0
        while(n):
            n=n & (n-1)
            count=count+1
        return(count)

h= hammingWeight()
n= 0o00000000000000000000000010000000
print(h.numofones(n))

#solution 2
class numberofones():
    def numofones(self,n):
        count = 0
        while(n):
            if(n&1):
                count=count+1
            n=n>>1
        return(count)
n=numberofones()
print(n.numofones(5))

