#21. Merge Two Sorted Lists
#You are given the heads of two sorted linked lists list1 and list2.
#Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.Return the head of the merged linked list.

class Listnode():
    def __init__(self,val):
        self.val = val
        self.next = None

class Mergelists():
    def mergingsortedlists(self,list1,list2):
        dummy = Listnode(0)
        temp = dummy

        while(list1 and list2):
            if(list1.val <list2.val):
                temp.next = list1
                list1= list1.next
                temp=temp.next
            else:
                temp.next = list2
                list2 = list2.next
                temp = temp.next
        if(list1):
            temp.next = list1
        if(list2):
            temp.next = list2
        return(dummy.next)

    def printlist(self,head):
        while(head):
            print(head.val)
            head=head.next

m = Mergelists()
l1 = Listnode(1)
l1.next= Listnode(2)
l1.next.next=Listnode(4)
l2 = Listnode(1)
l2.next = Listnode(3)
l2.next.next = Listnode(4)
m.printlist(m.mergingsortedlists(l1,l2))