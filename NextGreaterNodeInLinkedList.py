#1019. Next Greater Node In Linked List
#Given the head of a linked list with n nodes.
#For each node in the list, find the value of the next greater node.

class ListNode():
    def __init__(self,val):
        self.val=val
        self.next=None
class Linkedlist():
    def nextLargernode(self,head):
        nodeval=[]
        temp=head

        while(temp):
            nodeval.append(temp.val)
            temp=temp.next

        res=[0]*len(nodeval)
        stack=[]
        for i in range(0,len(nodeval)):
            while(stack and  nodeval[stack[-1]]<nodeval[i]):
                res[stack.pop()] = nodeval[i]
            stack.append(i)

        return(res)

head= ListNode(2)
head.next=ListNode(7)
head.next.next=ListNode(4)
head.next.next.next=ListNode(3)
head.next.next.next.next=ListNode(5)
l=Linkedlist()
print(l.nextLargernode(head))



