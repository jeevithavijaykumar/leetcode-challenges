class Buildingarray():
    def arraybuilder(self,target,num):
        res =[]
        for i in range(1,max(target)+1):
            if i in target:
                res.append('Push')
            else:
                res.append('Push')
                res.append('Pop')
        return(res)

b = Buildingarray()
target=[1,4,5]
print(b.arraybuilder(target,5))