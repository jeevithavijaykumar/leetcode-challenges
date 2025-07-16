# 392. Is Subsequence
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters
# without disturbing the relative positions of the remaining characters.
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution():
    def isSubsequence(self, s, t):
         i=0

         for char in t:
             if i<len(s) and s[i]==char:
                 i=i+1

         return i ==len(s)

s= Solution()
print(s.isSubsequence('ace','abcde'))
print(s.isSubsequence('aec','abcde'))