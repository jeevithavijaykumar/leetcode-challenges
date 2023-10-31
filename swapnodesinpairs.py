#24. Swap Nodes in Pairs
#Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)

class ListNode():
    def __init__(self,val):
        self.val = val
        self.next= None

class Linkedlist():
    def swappairs(self,head):
        dummy = ListNode(0)
        dummy.next=head
        cur=dummy

        while(cur.next and cur.next.next):
            first = cur.next
            second=cur.next.next
            cur.next=second
            first.next = second.next
            second.next =first
            cur =cur.next.next

        return(dummy.next)

    def printlist(self,node):
        temp=node
        while(temp):
            print(temp.val)
            temp=temp.next
        return


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
l = Linkedlist()
l.printlist(l.swappairs(head))


