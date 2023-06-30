#You are given an integer array coins representing coins of different denominations and
# an integer amount representing a total amount of money.
#Return the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.

class Coinchange():
    def dpcoinchange(self,coin,amount):
        DP=[amount+1]*(amount+1)
        DP[0]=0

        for a in range(1,amount+1):
            for c in coin:
                if(a-c >=0):
                    DP[a]=min(DP[a],1+DP[a-c])
        if(DP[amount]!=amount+1):
            return(DP[amount])
        else:
            return(-1)

c=Coinchange()
print(c.dpcoinchange([1,2,5],11))
