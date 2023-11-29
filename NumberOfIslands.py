#200. Number of Islands
#Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

import collections
class Grid():
    def numIslands(self,grid):
        rows=len(grid)
        cols=len(grid[0])
        islands=0
        visit=set()

        def bfs(r,c):
            visit.add((r,c))
            q = collections.deque()
            q.append((r,c))
            while(q):
                row,col = q.popleft()
                directions =[[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    r=row+dr
                    c=col+dc
                    if(r in range(0,rows) and c in range(0,cols) and
                        grid[r][c]=='1' and (r,c) not in visit):
                        visit.add((r,c))
                        q.append((r,c))

        for r in range(0,rows):
            for c in range(0,cols):
                if(grid[r][c]=='1' and (r,c) not in visit):
                    bfs(r,c)
                    islands+=1
        return(islands)

g=Grid()
print(g.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
