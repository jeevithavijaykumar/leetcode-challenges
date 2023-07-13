#326. Power of Three -- An integer n is a power of three, if there exists an integer x such that n == 3x.
#Given an integer n, return true if it is a power of three. Otherwise, return false.

class Powerofthree():
    def ispowerthree(self,n):
        if(n<=0):
            return(False)
        while(n%3==0):
            n=n/3
        return(n==1)
p=Powerofthree()
print(p.ispowerthree(27))

