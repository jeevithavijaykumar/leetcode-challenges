#Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
#Solution is to first convert the number to str and then to list, then use sum(list) to get the sum of digits

class Adddigits():
    def adddigits(self,num):

        while(num>9):
            num = sum(int(i) for i in list(str(num)))
        return(num)

a= Adddigits()
print(a.adddigits(5694))