#Intersection of Two Linked Lists
#Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
# If the two linked lists have no intersection at all, return null.


class IntersectingLinkedlists():
    def Intersection(self,headA, headB):
        a = headA
        b= headB

        while(a!=b):
            if(a!=None):
                a=a.next
            else:
                a = headB
            if(b!=None):
                b=b.next
            else:
                b = headA
        return(a)
i = IntersectingLinkedlists()
i.Intersection(a,b)


#Solution 2
class IntersectingLinkedlists():
    def Intersection(self,headA, headB):
        tempa = headA
        t1 = 0
        t2 = 0
        while (tempa):
            tempa = tempa.next
            t1 = t1 + 1

        tempb = headB

        while (tempb):
            tempb = tempb.next
            t2 = t2 + 1

        tempa1 = headA
        tempb1 = headB
        if (t1 > t2):
            t = t1 - t2
            while (t):
                tempa1 = tempa1.next
                t = t - 1

        elif (t2 > t1):
            t = t2 - t1
            while (t):
                tempb1 = tempb1.next
                t = t - 1

        while (tempa1 and tempb1):
            if (tempa1 == tempb1):
                return (tempa1)
            else:
                tempa1 = tempa1.next
                tempb1 = tempb1.next

i = IntersectingLinkedlists()
i.Intersection(a,b)

