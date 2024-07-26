""" 47. Permutations II """
""" Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order. """

from collections import Counter

class Solution:
    def permuteUnique(self,nums):
        permutations =[]
        counter = Counter(nums)

        def findallpermutations(res):
            if(len(res)==len(nums)):
                permutations.append(res)
                return

            for key in counter:
                if counter[key]:
                    counter[key] -=1
                    findallpermutations(res+[key])
                    counter[key]+=1

        findallpermutations([])
        return(permutations)

s=Solution()
print(s.permuteUnique([1,1,2]))

