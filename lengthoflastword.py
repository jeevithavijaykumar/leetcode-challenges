#58. Length of Last Word
#Given a string s consisting of words and spaces, return the length of the last word in the string.
#s consists of only English letters and spaces ' '

class Lengthoflastword():
    def findlength(self,s):
        if(s==''):
            return(0)
        s=s.rstrip()
        l=len(s)-1
        length =0
        while(l>=0):
            if(s[l].isalpha()):
                length= length+1
                l=l-1
            else:
                return(length)
        return(length)

l = Lengthoflastword()
s = 'Hello World'
print(l.findlength(s))

#Solution 2

class Lengthoflastword():
    def findlength(self,s):
        word = s.split()  #Split function splits the string into list contining words.To define seperator use,w = s.split(',')/ w = s.split('#')
        lenoflist = len(word)
        lastindex = lenoflist-1
        print(len(word[lastindex]))

l = Lengthoflastword()
s = 'Hello World'
print(l.findlength(s))

____________________________




