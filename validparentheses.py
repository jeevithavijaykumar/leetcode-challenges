#20. Valid Parentheses
#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
# Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.

class Validparentheses():
    def isvalid(self,s):
        stack=[]
        closetoopen={')':'(',']':'[','}':'{'}

        for i in s:
            if(i in closetoopen):
                if(stack and closetoopen[i]==stack[-1]):
                    stack.pop()
                else:
                    return(False)
            else:
                stack.append(i)

        return(False if(stack) else True)

v= Validparentheses()
print(v.isvalid("(]"))
