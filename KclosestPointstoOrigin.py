#973. K Closest Points to Origin
#Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
#Return the k closest points to the origin (0, 0).
#The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

import math
import heapq
class List:
    def kClosest(self, points, k):
        arr=[]
        for x,y in points:
            dist= math.sqrt((x)**2+(y)**2)
            arr.append([dist,x,y])

        heapq.heapify(arr)
        res=[]
        while(k):
            dist,x,y =heapq.heappop(arr)
            res.append([x,y])
            k=k-1
        return(res)

l = List()
print(l.kClosest([[3, 3], [5, -1], [-2, 4]], 2))

