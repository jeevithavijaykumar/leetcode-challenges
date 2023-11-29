#150. Evaluate Reverse Polish Notation
#Given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
#Evaluate the expression. Return an integer that represents the value of the expression.
class List:
    def evalRPN(self, tokens):
        s=[]

        for c in tokens:
            if(c=='+'):
                res=s.pop()+s.pop()
                s.append(res)
            elif(c=='-'):
                a=s.pop()
                b=s.pop()
                res=b-a
                s.append(res)
            elif(c=='*'):
                res=s.pop()*s.pop()
                s.append(res)
            elif(c=='/'):
                a=s.pop()
                b=s.pop()
                res=int(b/a)
                s.append(res)
            else:
                s.append(int(c))

        return(s[0])

l=List()
print(l.evalRPN(["2","1","+","3","*"]))
print(l.evalRPN(["4","13","5","/","+"]))