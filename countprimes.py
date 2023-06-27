#204. Count Primes
#Given an integer n, return the number of prime numbers that are strictly less than n.

class countPrimes():
    def countprimenum(self,n):
        res=[1]*n

        for i in range(0,n):
            if(i<=1):
                res[i]=0
            if(res[i]):
                for j in range(i*i,n,i):
                    res[j]=0
        return(sum(res))
c=countPrimes()
print(c.countprimenum(15))