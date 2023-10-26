#290  Word Pattern
#Given a pattern and a string s, find if s follows the same pattern.
#Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
#Input: pattern = "abba", s = "dog cat cat dog"  Output: true
#Input: pattern = "abba", s = "dog cat cat fish"  Output: false

class String():
    def wordpattern(self,s,pattern):
        d={}
        word = s.split()
        if(len(pattern)!=len(word)):
            return(False)

        for i in range(0,len(word)):
            if(pattern[i] in d):
                if(d[pattern[i]]!=word[i]):
                    return(False)
            elif(word[i] in d.values()):
                return(False)
            else: d[pattern[i]]=word[i]
        return(True)

s=String()
print(s.wordpattern("dog cat cat dog","abba"))

