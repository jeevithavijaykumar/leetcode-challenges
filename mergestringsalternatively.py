#1768. Merge Strings Alternately
#You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
#If a string is longer than the other, append the additional letters onto the end of the merged string.
#Return the merged string.

class Strings():
    def mergestrings(self,word1,word2):
        l1=list(word1)
        l2=list(word2)
        res=[]

        for i in range(0,len(word1+word2)):
            if(i<len(l1)):
                res.append(l1[i])
            if(i<len(l2)):
                res.append(l2[i])
        return(''.join(str(e) for e in res))

s=Strings()
print(s.mergestrings('ab','pqrs'))

