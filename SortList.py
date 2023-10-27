#148. Sort List
#Given the head of a linked list, return the list after sorting it in ascending order.

class ListNode():
    def __init__(self,val):
        self.next=None
        self.val=val

class Sortlinkedlist():
    def sortlist(self,head):
        if not head or not head.next:
            return head

        left = head
        right = self.getmid(head)
        temp = right.next
        right.next = None
        right = temp
        left = self.sortlist(left)
        right = self.sortlist(right)
        return (self.mergelist(left, right))

    def getmid(self, head):
        slow = head
        fast = head.next
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        return (slow)

    def mergelist(self, left, right):
        tail = dummy = ListNode(0)
        while (left and right):
            if (left.val < right.val):
                dummy.next = left
                left = left.next
                dummy = dummy.next
            else:
                dummy.next = right
                right = right.next
                dummy = dummy.next
        if (left):
            dummy.next = left
        elif (right):
            dummy.next = right
        return (tail.next)

    def printlist(self,head):
        temp1=head
        while(temp1):
            print(temp1.val)
            temp1=temp1.next
        return

head=ListNode(4)
head.next = ListNode(2)
head.next.next =ListNode(1)
head.next.next.next = ListNode(3)
s= Sortlinkedlist()
s.printlist(s.sortlist(head))