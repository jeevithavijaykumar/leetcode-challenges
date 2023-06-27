#Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.#
# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].
#For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

class Buddystrings():
    def buddystr(selfself,s,goal):
        diff=[]

        if(len(s)!=len(goal)):
            return(False)
        if(s==goal and len(set(s))<len(s)):
            return(True)
        for i in range(0,len(s)):
            if(s[i]!=goal[i]):
                diff.append([s[i],goal[i]])
        if(len(diff)==2 and diff[0]==diff[1][::-1]):
            return(True)
        return(False)

b =Buddystrings()
print(b.buddystr('aabc','aabc'))



