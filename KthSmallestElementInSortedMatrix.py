#378. Kth Smallest Element in a Sorted Matrix
#Given an n x n matrix where each of the rows and columns is sorted in ascending order,
#Return the kth smallest element in the matrix.

from bisect import bisect_right
class Matrix():
    def kthsmallest(self,matrix,k):
        l=matrix[0][0]
        r=matrix[-1][-1]

        def helperfn(m):
            count=0
            for i in range(0,len(matrix)):
                x=bisect_right(matrix[i],m)
                count=count+x
            return(count)

        while(l<=r):
            mid=(l+r)//2
            if(helperfn(mid)<k):
                l=mid+1
            else:
                r=mid-1
        return(l)

m=Matrix()
print(m.kthsmallest([[1,5,9],[10,11,13],[12,13,15]],8))
print(m.kthsmallest([[-5]],1))