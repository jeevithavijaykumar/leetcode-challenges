# Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.


class ListNode():
    def __init__(self, val=0, next =None):
        self.val = val
        self.next = next

class Solution():
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 != None or l2 != None or carry != 0:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0

            columnsum = l1val + l2val + carry
            carry = columnsum // 10
            newnode = ListNode(columnsum % 10)
            curr.next = newnode
            curr = newnode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

def list_to_linkedlist(lst):
    dummy = ListNode(0)
    curr = dummy

    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linkedlist_to_list(node):
    res = []
    while (node):
        res.append(node.val)
        node = node.next
    return res

s = Solution()
l1 = list_to_linkedlist([2,4,3])
l2 = list_to_linkedlist([5,6,4])
result = s.addTwoNumbers(l1,l2)
print(linkedlist_to_list(result))

