#542. 01 Matrix
#Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
#The distance between two adjacent cells is 1.

import collections
class Matrix():
    def updatematrix(self,mat):
        rows = len(mat)
        cols = len(mat[0])
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if (mat[r][c] == 0):
                    q.append((r, c))
                else:
                    mat[r][c] = '#'

        while (q):
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                r = row + dr
                c = col + dc
                if (r in range(rows) and c in range(cols) and mat[r][c] == '#'):
                    mat[r][c] = mat[row][col] + 1
                    q.append((r, c))

        return(mat)

m=Matrix()
print(m.updatematrix([[0,0,0],[0,1,0],[1,1,1]]))