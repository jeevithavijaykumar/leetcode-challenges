#Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
#Two Approaches
#First approach is to convert linkedlist to array. Use left and right pointers to determine if it is a palindrome.

#Approach 1


from LinkedListRepresentation import Linkedlist

class Linkedlistpalindrome():
    def palindrome(self):
        nums =[]
        temp1 = head
        while(temp1):
            nums.append(temp1.data)
            temp1 = temp1.next
        l=0
        r=len(nums)-1
        
        while(l<=r):
            if(nums[l]!=nums[r]):
                return(False)
            l=l+1
            r=r-1
        return(True)
    
l = Linkedlistpalindrome()
print(l.palindrome())