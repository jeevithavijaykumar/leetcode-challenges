#Find K Closest Elements
#Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
# The result should also be sorted in ascending order.

class Closestelements():
    def closestkelements(self,arr,k,x):
        l = 0
        r = len(arr)-k

        while(l<r):
            mid = int((l+r)/2)
            if((x-arr[mid]) > (arr[mid+k]-x)):
                l =mid+1
            else:
                r=mid
        return(arr[l:l+k])

c =Closestelements()
arr=[1,2,3,4,5]
print(c.closestkelements(arr,2,5))