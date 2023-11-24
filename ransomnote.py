#383. Ransom Note
#Given two strings ransomNote and magazine,return true if ransomNote can be constructed by using the letters from magazine
# and false otherwise. Each letter in magazine can only be used once in ransomNote.

class String():
    def canconstruct(self,ransomnote,magazine):
        d={}

        for i in range(0,len(magazine)):
            d[magazine[i]]=1+d.get(magazine[i],0)

        for j in range(0,len(ransomnote)):
            if(ransomnote[j] not in d):
                return(False)
            elif(d[ransomnote[j]]==0):
                return(False)
            else:
                d[ransomnote[j]]=d[ransomnote[j]]-1
        return(True)

s=String()
print(s.canconstruct("aa","ab"))
print(s.canconstruct("aa","aab"))
print(s.canconstruct("a","b"))