#435. Non-overlapping Intervals
#Given an array of intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

class Intervals():
    def nonoverlappingintervals(self,intervals):
        intervals.sort(key=lambda i:i[1])
        count=0
        prev= intervals[0]
        for i in range(1,len(intervals)):
            if(intervals[i][0]<prev[1]):
                count=count+1
            else:
                prev = intervals[i]
        return(count)

i=Intervals()
print(i.nonoverlappingintervals([[1,2],[2,3],[2,5],[6,40],[1,100]]))