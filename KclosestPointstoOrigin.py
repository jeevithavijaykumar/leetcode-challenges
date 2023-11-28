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

