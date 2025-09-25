# You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat,
# and seats[i] = 0 represents that the ith seat is empty (0-indexed).
# There is at least one empty seat, and at least one person sitting.
# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.
# Return that maximum distance to the closest person.

class Solution:
    def maxDistToClosest(self, seats):
        prev = -1
        maxdist = 0

        for i, seat in enumerate(seats):
            if(seat==1):
                if(prev==-1):
                    maxdist = i
                else:
                    maxdist = max(maxdist, (i-prev)//2)
                prev = i

        maxdist = max(maxdist, len(seats)-1-prev)
        return maxdist

s= Solution()
print(s.maxDistToClosest([1,0,0,0,1,0,1]))
print(s.maxDistToClosest([1,0,0,0]))