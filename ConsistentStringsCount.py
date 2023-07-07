#1684. Count the Number of Consistent Strings
#You are given a string allowed consisting of distinct characters and an array of strings words.
# A string is consistent if all characters in the string appear in the string allowed.
# Return the number of consistent strings in the array words.

class Consistentstring():
    def consistenstr(self,allowed,words):
        consistentstrcnt=len(words)

        for i in range(0,len(words)):
            for j in range(0,len(words[i])):
                if(words[i][j] not in allowed):
                    consistentstrcnt= consistentstrcnt-1
                    print(words[i][j])
                    print(i)
                    print(consistentstrcnt)
                    break
        return(consistentstrcnt)

c=Consistentstring()
allowed ="cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]
print(c.consistenstr(allowed,words))