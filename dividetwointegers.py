#29. Divide Two Integers
#Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
#The integer division should truncate toward zero, which means losing its fractional part.
#Return the quotient after dividing dividend by divisor.
#if the quotient is strictly greater than 231 - 1,
# then return 2**31 - 1, and if the quotient is strictly less than -23**1, then return -23**1.

class Integers():
    def dividetwointegers(self,dividend,divisor):
        d=abs(dividend)
        dv = abs(divisor)
        output=0

        while(d>=dv):
            temp = dv
            mult=1
            while(d>=temp):
                d=d-temp
                output=output+mult
                mult=mult+mult
                temp=temp+temp
        if(dividend<0 and divisor>=0) or (dividend>=0 and divisor<0):
            output=-output
        return(min((2^31)-1,max((-2)^31,output)))

i = Integers()
print(i.dividetwointegers(35,-3))