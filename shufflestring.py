#1528. Shuffle String
#You are given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
#Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
#Output: "leetcode

class Shuffelstring():
    def shufflestr(self,s,indices):
        op=['']*len(s)
        count=0
        for i in indices:
            op[i]=s[count]
            count=count+1
        return(''.join(str(ele) for ele in op))

s=Shuffelstring()
print(s.shufflestr('codeleet',[4,5,6,7,0,2,1,3]))