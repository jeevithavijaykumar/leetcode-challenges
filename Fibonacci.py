class Fibonacci():
    def fib(self,n):
        if(n==0):
            return(0)
        if(n==1):
            return(1)
        if(n==2):
            return(1)
        if(n==3):
            return(2)
        if(n==4):
            return(3)
        if(n==5):
            return(5)
        else:
            return(self.fib(n-1)+self.fib(n-2))

f =Fibonacci()
print(f.fib(10))