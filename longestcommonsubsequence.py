#1143. Longest Common Subsequence
#Given two strings text1 and text2, return the length of their longest common subsequence.
# If there is no common subsequence, return 0.
#A subsequence of a string is a new string generated from the original string with some characters (can be none)
# deleted without changing the relative order of the remaining characters.

class LongestCommonSubsequence():
    def LCS(self,text1,text2):
        DP=[[0 for j in range(0,len(text2)+1)] for i in range(0,len(text1)+1)]

        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if(text1[i]==text2[j]):
                    DP[i][j]=1+DP[i+1][j+1]
                else:
                    DP[i][j]=max(DP[i][j+1],DP[i+1][j])
        return(DP[0][0])

l=LongestCommonSubsequence()
print(l.LCS('abcde','ace'))








