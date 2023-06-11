#Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Approach is to use the first string in the lisr as reference and start comparing each letter in first string against the others.
#once letter matches with the the strings in the list add it to result, and continue with the rest. Once it does not match, return result.
#Also, when second or third string is smaller than first, return the result as that would be your longest common prefix.

class Longestcommonprefix():
    def longestprefix(self,strs):
        prefix =''
        for i in range(0,len(strs[0])):
            for j in range(0,len(strs)):
                if(i<len(strs[j]) and strs[0][i]==strs[j][i]):
                    if(j==len(strs)-1):
                        prefix = prefix + strs[0][i]
                else:
                    return(prefix)
        return(prefix)

l = Longestcommonprefix()
strs = ['flow','flower','flu']
print(l.longestprefix(strs))
