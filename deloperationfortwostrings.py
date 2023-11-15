#583. Delete Operation for Two Strings
#Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

class deleteforstrings():
    def deletestrings(self,word1,word2):
        DP=[[0 for j in range(0,len(word2)+1)] for i in range(0,len(word1)+1)]

        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if(word1[i-1]==word2[j-1]):
                    DP[i][j]=1+DP[i-1][j-1]
                else:
                    DP[i][j]=max(DP[i][j-1],DP[i-1][j])
        return(len(word1)+len(word2)-2*(DP[len(word1)][len(word2)]))
    
d=deleteforstrings()
print(d.deletestrings("leetcode","etco"))


