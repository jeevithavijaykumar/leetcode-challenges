#118. Pascal's Triangle
#Given an integer numRows, return the first numRows of Pascal's triangle.

class Pascalstrinagle():
    def pascal(self,numrows):
        res=[[1]]


        for i in range(0,numrows-1):
            row=[]
            temp=[0]+res[-1]+[0]
            for j in range(0,len(res[-1])+1):
                row.append(temp[j]+temp[j+1])
            res.append(row)
        return(res)

p=Pascalstrinagle()
print(p.pascal(5))

