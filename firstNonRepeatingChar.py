# Write a Python function that takes a string and returns the first non-repeating character.
# If all characters repeat, return None.


class Solution:
    def fistNonrepeatingChar(self, s):
        freq = {}

        for c in s:
            freq[c] = freq.get(c,0) + 1

        for char in s:
            if freq[char] == 1 :
                return char
        return None

if __name__ == "__main__" :
    s= Solution()
    print(s.fistNonrepeatingChar("swiss"))
    print(s.fistNonrepeatingChar("people"))