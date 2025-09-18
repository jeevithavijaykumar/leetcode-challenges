# You are given a string s consisting of lowercase English letters.
# A duplicate removal consists of choosing two adjacent and equal letters and removing them.
# We repeatedly make duplicate removals on s until we no longer can.
# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

class Solution:
    def removeDuplicates(self, s):

        output = []

        for ch in s:
            if(output and (ch == output[-1])):
                output.pop()
            else:
                output.append(ch)

        return "".join(c for c in output)

s= Solution()
print(s.removeDuplicates("abbaca"))
print(s.removeDuplicates("azxxzy"))