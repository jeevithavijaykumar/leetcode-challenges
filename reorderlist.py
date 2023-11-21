#143. Reorder List
#You are given the head of a singly linked-list. The list can be represented as: L0 → L1 → … → Ln - 1 → Ln
#Reorder the list to be on the following form: L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 ..
class Listnode():
    def __init__(self,val):
        self.val=val
        self.next=None
class Linkedlist():
    def reorderlist(self,head):
        if (not head or not head.next):
            return (head)

        # find mid
        slow = head
        fast = head
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        #Reversing the second half of the list
        cur = slow.next
        prev = None
        while (cur):
            curnext = cur.next
            cur.next = prev
            prev = cur
            cur = curnext
        slow.next = None

        #Merge first and second half
        head2 = prev
        head1 = head
        while (head2):
            nexxt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nexxt
        return (head)
    def printlist(self,node):
        temp=node
        res=[]
        while(temp):
            res.append(temp.val)
        return(res)

head=Listnode(1)
head.next=Listnode(2)
head.next.next=Listnode(3)
head.next.next.next=Listnode(4)
head.next.next.next.next=Listnode(5)
l=Linkedlist()
print(l.printlist(l.reorderlist(head)))