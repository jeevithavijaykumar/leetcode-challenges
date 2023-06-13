#Convert Binary Number in a Linked List to Integer.Given head which is a reference node to a singly-linked list.
# The value of each node in the linked list is either 0 or 1.The linked list holds the binary representation of a number.

class BinaryLinkedlist():
    def Binary(self,head):
        sum = 0
        temp = head
        while(temp):
            sum = sum*2 + temp.val
            temp = temp.next

        return(sum)