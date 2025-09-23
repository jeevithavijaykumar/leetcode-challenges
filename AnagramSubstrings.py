# Given two strings s and p, return all starting indices of substrings in s that are anagrams of p.

from collections import Counter

class Solution:
    def anagramSubstrings(self, s, p):
        if(len(s)<len(p)):
            return []

        k = len(p)
        res =[]
        map_p = Counter(p)
        window_map = Counter(s[:k])

        if(window_map == map_p):
            res.append(0)

        for i in range(k,len(s)):
            window_map[s[i]] = window_map[s[i]]+1
            window_map[s[i-k]] = window_map[s[i-k]]-1
            if(window_map[s[i-k]] ==0):
                del window_map[s[i-k]]
            if(window_map == map_p):
                res.append(i-k+1)
        return res

s= Solution()
print(s.anagramSubstrings("cbaebabacd", "abc"))
