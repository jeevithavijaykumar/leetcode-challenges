# 266 Palindrome Permutation
# Given a string s, return true if a permutation of the string could form a palindrome and false otherwise.

# Example 1:
# Input: s = "code"
# Output: false

class Solution():
    def canPermutePalindrome(self,s):

        sets= set()

        for char in s:
            if char not in sets:
                sets.add(char)
            else:
                sets.remove(char)

        return len(sets)<=1

s= Solution()
print(s.canPermutePalindrome("aab"))



