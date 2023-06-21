#7. Reverse Integer
#Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Reverseinteger():
    def reverse(self,x):
        res = 0
        sign = 1
        if (x < 0):
            x=0-x
            sign = -1
        s = list(str(x))

        for i in range(len(s) - 1, -1, -1):
            res = res * 10 + (ord(s[i]) - ord('0'))

        res = res * sign
        if (res > (2 ** 31 - 1) or res < ((-2) ** 31)):
            return (0)
        else:
            return (res)
r=Reverseinteger()
print(r.reverse(-523))
