#733. Flood Fill
#An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
#You are also given three integers sr, sc, and color.
#You should perform a flood fill on the image starting from the pixel image[sr][sc].
#Return the modified image after performing the flood fill.

import collections
class Matrix():
    def floodfill(self,image,sr,sc,color):
        q = collections.deque()
        rows = len(image)
        cols = len(image[0])
        visit = set()
        q.append((sr, sc))
        start_color = image[sr][sc]
        image[sr][sc] = color

        while (q):
            row, col = q.popleft()
            visit.add((row, col))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                r = row + dr
                c = col + dc
                if (r in range(rows) and c in range(cols) and
                        (r, c) not in visit and image[r][c] == start_color):
                    image[r][c] = color
                    q.append((r, c))
        return (image)

m=Matrix()
print(m.floodfill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))