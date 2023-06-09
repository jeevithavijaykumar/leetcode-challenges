#69. Sqrt(x)
#Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.

class Mysqrt():
    def squareroot(self,x):
        low =0
        high=x
        while(low<=high):
            mid = (low+high)/2

            if(mid*mid > x):
                high =mid-1
            elif(mid*mid < x):
                low = mid+1
            else:
                return(mid)
        return(int(high))

m = Mysqrt()
print(m.squareroot(15))