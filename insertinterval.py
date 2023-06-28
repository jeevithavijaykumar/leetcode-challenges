#57. Insert Interval
#You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
# You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
#Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

class Insertinterval():
    def insert(self,intervals,newInterval):
        output=[]

        for i in range(0,len(intervals)):
            if(newInterval[1]<intervals[i][0]):
                output.append(newInterval)
                return(output+intervals[i:])
            elif(intervals[i][1]<newInterval[0]):
                output.append(intervals[i])
            else:
                newInterval=[min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]

        output.append(newInterval)
        return(output)

i=Insertinterval()
print(i.insert([[1,3],[6,9]],[2,5]))