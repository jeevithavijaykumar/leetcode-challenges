#28. Find the Index of the First Occurrence in a String
#Given two strings needle and haystack,
# return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#Input: haystack = "sadbutsad", needle = "sad"    #Output: 0

class Firstoccurence():
    def firstoccreneceinstring(self,haystack,needle):
        for i in range(0,len(haystack)+len(needle)+1):
            for j in range(0,len(needle)):
                if(haystack[i+j]!=needle[j]):
                    break
                if(j==len(needle)-1):
                    return(i)
        return(-1)
f=Firstoccurence()
print(f.firstoccreneceinstring("hello","ll"))

#Solution2

class Firstoccurence():
    def firstoccurenceinstr(self,haystack,needle):
        if(len(needle)>len(haystack)):
            return(-1)
        for i in range(0,len(haystack)):
            for j in range(0,len(needle)):
                if((i+j) > len(haystack)-1):
                    return(-1)
                if(needle[j]==haystack[i+j]):
                    if(j==len(needle)-1):
                        return(i)
                else:
                    break
f= Firstoccurence()
print(f.firstoccurenceinstr('sadbutsad','sad'))




