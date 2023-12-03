#70. Climbing Stairs
#You are climbing a staircase. It takes n steps to reach the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top.

class Climbingstairs():
    def noofways(self,n):
        dp = [0] * (n + 1)
        if (n==0):
            return(0)
        if (n==1):
            return(1)
        if (n==2):
            return(2)
        dp[0]=0
        dp[1]=1
        dp[2]=2
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return (dp[n])

c=Climbingstairs()
print(c.noofways(5))






