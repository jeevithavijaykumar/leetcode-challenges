# You are given an integer money denoting the amount of money (in dollars) that you have
# and another integer children denoting the number of children that you must distribute the money to.
# You have to distribute the money according to the following rules:
# All money must be distributed.
# Everyone must receive at least 1 dollar.
# Nobody receives 4 dollars.
# Return the maximum number of children who may receive exactly 8 dollars if you distribute the money according to the aforementioned rules.
# If there is no way to distribute the money, return -1.


class Solution():
    def distMoney(selfself, money, children):

        if(money < children):
            return -1
        if (money > children*8):
            return children - 1
        res = 0
        while( (money>0) and ((money-8) >= children-1)):
            money = money-8
            children = children -1
            res = res+1

        if(money == 4 and children ==1):
            res = res -1

        return res

s = Solution()
print(s.distMoney(20))
print(s.distMoney(16))
