#48. Rotate Image
#You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

class Matrix():
    def rotateimage(self,matrix):
        l= 0
        r= len(matrix)-1

        while(l<r):
            top = l
            bottom = r
            for i in range(0,r-l):
                topleft = matrix[top][l+i]
                matrix[top][l+i] = matrix[bottom-i][l]
                matrix[bottom-i][l] = matrix[bottom][r-i]
                matrix[bottom][r-i] = matrix[top+i][r]
                matrix[top+i][r] = topleft
            l=l+1
            r=r-1
m = Matrix()
a = [[1,2,3],[4,5,6],[7,8,9]]
m.rotateimage(a)
print(a)

