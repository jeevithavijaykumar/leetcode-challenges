#19. Remove Nth Node From End of List
#Given the head of a linked list, remove the nth node from the end of the list and return its head.

class Listnode():
    def __init__(self,val):
        self.val=val
        self.next=None

class Linkedlist():
    def removenthfromend(self,head,n):
        dummy=Listnode(0)
        dummy.next=head
        left=dummy
        right=head

        while(n):
            right=right.next
            n=n-1
        while(right):
            left=left.next
            right=right.next
        left.next=left.next.next
        return(dummy.next)

    def printlist(self,node):
        temp=node
        res=[]
        while(temp):
            res.append(temp.val)
            temp=temp.next
        return(res)

head=Listnode(1)
head.next=Listnode(2)
head.next.next=Listnode(3)
head.next.next.next=Listnode(4)
head.next.next.next.next=Listnode(5)
l=Linkedlist()
print(l.printlist(l.removenthfromend(head,2)))

