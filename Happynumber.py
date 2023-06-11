#Write an algorithm to determine if a number n is happy.
#A happy number is a number defined by the following process:
#Starting with any positive integer, replace the number by the sum of the squares of its digits.
#Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#Those numbers for which this process ends in 1 are happy.
#Return true if n is a happy number, and false if not.

class Happynumber():
    def happynumber(self,n):
        mem= set()
        while(n!=1):
            n = sum(int(i)*int(i) for i in list(str(n)))
            if(n in mem):
                return(False)
            else:
                mem.add(n)
        return(True)

h = Happynumber()
print(h.happynumber(19))

