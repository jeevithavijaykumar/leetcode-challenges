#92. Reverse Linked List II
#Given the head of a singly linked list and two integers left and right where left <= right,
# reverse the nodes of the list from position left to position right, and return the reversed list.

class Node():
    def __init__(self,data):
        self.data = data
        self.next=None

class linkedlist():
    def __init(self):
        self.head = None

    def reverselist(self,left,right):
        dummy =Node(0)
        dummy.next=self.head
        curr =self.head
        lp=dummy
        for i in range(0,left-1):
            curr=curr.next
            lp=lp.next
        prev=None
        for j in range(0,(right-left+1)):
            tempnext =curr.next
            curr.next=prev
            prev = curr
            curr=tempnext

        lp.next.next=curr
        lp.next=prev

    def Printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp = temp.next

llist = linkedlist()
llist.head = Node(1)
second= Node(2)
third= Node(3)
forth= Node(4)
fifth=Node(5)
llist.head.next = second
second.next=third
third.next=forth
forth.next=fifth
llist.Printlist()
llist.reverselist(2,4)
llist.Printlist()
