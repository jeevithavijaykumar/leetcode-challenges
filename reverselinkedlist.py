#206. Reverse Linked List
#Given the head of a singly linked list, reverse the list, and return the reversed list.
class ListNode():
    def __init__(self,val):
        self.val=val
        self.next=None
class Linkedlist():
    def reverselist(self,head):
        temp=head
        prev=None

        while(temp):
            tempnext=temp.next
            temp.next=prev
            prev=temp
            temp=tempnext
        return(prev)

    def printlist(self,node):
        temp=node
        while(temp):
            print(temp.val)
            temp=temp.next

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)
l=Linkedlist()
l.printlist(l.reverselist(head))
