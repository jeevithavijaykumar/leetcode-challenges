#121. Best Time to Buy and Sell Stock
#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Buysellstock():
    def buysell(self,prices):
        l=0
        r=1
        maxprofit=0
        while(r<len(prices)):
            if(prices[l]<prices[r]):
                profit=prices[r]-prices[l]
                maxprofit=max(profit,maxprofit)
                r=r+1
            else:
                l=r
                r=r+1
        return(maxprofit)

b=Buysellstock()
prices=[2,4,1]
print(b.buysell(prices))

