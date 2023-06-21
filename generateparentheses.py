#22. Generate Parentheses
#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Generrateparentheses():
    def parenthesesgenerator(self,n):
        res=[]
        stack=[]

        def backstrap(openn,closedn):
            if(openn==closedn==n):
                res.append(''.join(stack))
                return
            if(openn<n):
                stack.append('(')
                backstrap(openn+1,closedn)
                stack.pop()
            if(closedn<openn):
                stack.append(')')
                backstrap(openn,closedn+1)
                stack.pop()
        backstrap(0,0)
        return(res)
g=Generrateparentheses()
print(g.parenthesesgenerator(3))



