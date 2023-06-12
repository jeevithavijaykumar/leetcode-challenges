#Given head, the head of a linked list, determine if the linked list has a cycle in it.
#There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer
#Lets use Flyod's Tortise and Hare algorithm. Two pointers Slow and fast. Slow pointer gets incremented once and fast twice.
#If there is a cycle then fast meets slow,hence return True. Otherwise fast or fast.next will be Null(indicating no cycle) hence return False.

class Linkedlist():
    def Hascycle(self,head) -> bool:
        slow = head
        fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if(slow==fast):
                return(True)
        return(False)


