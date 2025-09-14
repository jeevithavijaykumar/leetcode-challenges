#You are given a list of intervals represented as tuples/lists [start, end].
# Merge all overlapping intervals and return a list of the merged intervals.

class Solution:
    def mergeIntervals(self, intervals):

        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for interval in intervals[1:]:
            if(result[-1][1] >= interval[0]):
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        return result

s= Solution()
print(s.mergeIntervals([[1,3],[2,6],[8,10],[15,18]]))
print(s.mergeIntervals([[1,4],[4,5]]))