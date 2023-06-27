#204. Count Primes
#Given an integer n, return the number of prime numbers that are strictly less than n.

class countPrimes():
    def countprimenum(self,n):
        res=[1]*n
        res[0]=0
        res[1]=0

        for i in range(2,int(n**0.5)+1):
            if(res[i]):
                for j in range(i*i,n,i):
                    res[j]=0
        return sum(res)
c=countPrimes()
print(c.countprimenum(15))