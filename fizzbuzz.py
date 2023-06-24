#412. Fizz Buzz
#Given an integer n, return a string array answer (1-indexed) where:
#answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#answer[i] == "Fizz" if i is divisible by 3.
#answer[i] == "Buzz" if i is divisible by 5.
#answer[i] == i (as a string) if none of the above conditions are true.

class Fizzbuzz():
    def fizzbuzzprint(self,n):
        res=[]
        fizz,buzz=0,0
        for n in range(1,n+1):
            fizz=fizz+1
            buzz=buzz+1
            if(fizz==3 and buzz==5):
                res.append('Fizzbuzz')
                fizz=0
                buzz=0
            elif(fizz==3):
                res.append('Fizz')
                fizz=0
            elif(buzz==3):
                res.append('Buzz')
                buzz=0
            else:
                res.append(str(n))
        return(res)
r=Fizzbuzz()
print(r.fizzbuzzprint(8))