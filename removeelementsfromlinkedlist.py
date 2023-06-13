#Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val,
# and return the new head.

class Removeelementslinkedist():
    def Removeelements(self,head,val):
        while(head and head.val == val):
            head = head.next
        temp = head
        while(temp and temp.next):
            if(temp.next.val == val):
                temp.next=temp.next.next
            else:
                temp=temp.next

        return(head)


