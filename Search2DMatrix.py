#74. Search a 2D Matrix
#You are given an m x n integer matrix matrix with the following two properties:
#Each row is sorted in non-decreasing order.
#The first integer of each row is greater than the last integer of the previous row.
#Given an integer target, return true if target is in matrix or false otherwise.

class Matrix():
    def searchamatrix(self,matrix,target):
        row=len(matrix)
        col=len(matrix[0])

        t=0
        b=row-1
        while(t<=b):
            midrow=(t+b)//2
            if(target>matrix[midrow][-1]):
                t=midrow+1
            elif(target<matrix[midrow][0]):
                b=midrow-1
            else:
                break

        if(not t<=b):
            return(False)

        midrow=(t+b)//2
        l=0
        r=col-1
        while(l<=r):
            midcol=(l+r)//2
            if(target>matrix[midrow][midcol]):
                l=midcol+1
            elif(target<matrix[midrow][midcol]):
                r=midrow-1
            else:
                return(True)
        return(False)

m=Matrix()
print(m.searchamatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
print(m.searchamatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],35))


