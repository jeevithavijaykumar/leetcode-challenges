#1716. Calculate Money in Leetcode Bank
#X starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
#Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.
class Bank():
    def totalMoney(self, n):
        if(n==0):
            return(0)
        res=0
        monday=0
        nextday=0

        for i in range(0,n):
            if(i==0 or i%7==0):
                monday=monday+1
                res=res+monday
                nextday=monday+1
            else:
                res=res+nextday
                nextday=nextday+1
        return(res)

b=Bank()
print(b.totalMoney(10))

