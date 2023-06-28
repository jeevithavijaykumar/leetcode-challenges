#56. Merge Intervals
#Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# return an array of the non-overlapping intervals that cover all the intervals in the input.

class Mergeintervals():
    def intervalsmerge(self,intervals ):
        intervals.sort(key=lambda i:i[0])
        output = [intervals[0]]
        for i in range(1,len(intervals)):
            if(intervals[i][0] <= output[-1][1]):
                output[-1][1] = max(intervals[i][1],output[-1][1])
            else:
                output.append(intervals[i])
        return(output)

m=Mergeintervals()
print(m.intervalsmerge([[1,3],[2,6],[6,10],[15,18]]))


