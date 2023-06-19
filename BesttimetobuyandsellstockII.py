#122. Best Time to Buy and Sell Stock II
#You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
#On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
# However, you can buy it then immediately sell it on the same day.

class BesttimetoBuy():
    def isbesttime(self,prices):
        max_profit =0
        l=0
        r=1
        while (r < len(prices)):
            if (prices[l] < prices[r]):
                max_profit = max_profit + prices[r] - prices[l]
            l = r
            r = r + 1
        return (max_profit)
b=BesttimetoBuy()
print(b.isbesttime([7,1,5,3,6,4]))


