#66. Plus One
#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order.
#Increment the large integer by one and return the resulting array of digits.

class Numberplusone():
    def numberplusonearray(self,digits):
        num =0
        length = len(digits)

        for i in range(0,length):
            num = num + digits[i]*pow(10,(length-1-i))

        num = num+1

        return[int(i) for i in str(num)]

n = Numberplusone()
digits =[1,2,3]
print(n.numberplusonearray(digits))

