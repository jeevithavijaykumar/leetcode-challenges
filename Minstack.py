class Stack():
    def __init__(self):
        self.stack=[]
        self.minstack=[]

    def push(self,val):
        self.stack.append(val)
        minval= min(val,self.minstack[-1]) if self.minstack else val
        self.minstack.append(minval)

    def pop(self):
        if(len(self.stack)>0):
            self.stack.pop()
            self.minstack.pop()
        else:
            print('stack is empty')

    def top(self):
        if(len(self.stack)>0):
            return(self.stack[-1])
        else:
            print('Stack is empty')

    def get_min(self):
        if(len(self.minstack)>0):
            return(self.minstack[-1])
        else:
            print('stack is empty')

m = Stack()
m.push(10)
m.push(8)
m.push(50)
print(m.get_min())
m.push(5)
m.push(3)
m.pop()
print(m.get_min())





