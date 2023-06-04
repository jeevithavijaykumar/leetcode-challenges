#2. Add Two Numbers
#You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode():
    def __init__(self,val):
        self.next = None
        self.val = val

class Addtwonum():
    def addtwolinkedlists(self,l1,l2):
        dummy = ListNode(0)
        curr = dummy
        carry=0

        while(l1 or l2):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 +val2 + carry
            carry = sum // 10
            dig = sum%10
            curr.next = ListNode(dig)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if(carry):
            curr.next = ListNode(carry)
        return(dummy.next)

    def print_listnode(self,head):
        temp =head
        while(temp):
            print(temp.val)
            temp = temp.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
a=Addtwonum()
a.print_listnode(a.addtwolinkedlists(l1,l2))






