#994. Rotting Oranges
#Given an m x n grid where each cell can have one of three values: 0 -empty cell, 1 - fresh orange, 2 - rotten orange.
#Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
#Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

import collections
class Matrix():
    def orangesrotting(self,grid):
        rows=len(grid)
        cols=len(grid[0])
        rotten = collections.deque()
        freshcount=0
        minute=0

        for r in range(rows):
            for c in range(cols):
                if(grid[r][c]==2):
                    rotten.append((r,c))
                elif(grid[r][c]==1):
                    freshcount +=1

        while(rotten and freshcount>0):
            for i in range(0,len(rotten)):
                row,col = rotten.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if(r not in range(rows) or c not in range(cols)
                        or grid[r][c]==2 or grid[r][c]==0):
                        continue
                    else:
                        grid[r][c]=2
                        freshcount=freshcount-1
                        rotten.append((r,c))
            minute=minute+1

        if(freshcount==0):
            return(minute)
        else:
            return(-1)

m=Matrix()
print(m.orangesrotting([[2,1,1],[1,1,0],[0,1,1]]))
print(m.orangesrotting([[0,2]]))


