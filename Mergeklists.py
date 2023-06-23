#23. Merge k Sorted Lists
#You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#Merge all the linked-lists into one sorted linked-list and return it.

class ListNode():
    def __init(self,val):
        self.val = val
        self.next = None

class Sortedlists():
    def mergeklists(self,lists):
        if(not lists or len(lists)==0):
            return None

        while(len(lists)>1):
            mergelist =[]
            for i in range(0,len(lists),2):
                l1 = lists[i]
                if(i+1 <len(lists)):
                    l2 = lists[i+1]
                else:
                    l2 = None
                mergelist.append(self.mergetwolists(l1,l2))
            lists = mergelist
        return(lists[0])

    def mergetwolists(self,l1,l2):
        dummy = ListNode(0)
        temp = dummy
        while(l1 and l2):
            if(l1.val <l2.val):
                temp.next = l1
                l1=l1.next
            else:
                temp.next = l2
                l2=l2.next
            temp=temp.next
        if(l1):
            temp.next = l1
        if(l2):
            temp.next = l2
        return(dummy.next)


