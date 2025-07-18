# 243. Shortest Word Distance
# Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2,
# return the shortest distance between these two words in the list.


class Solution():
    def shortestDistance(self, wordsDict, word1, word2):

        index1 = -1
        index2 = -1
        min_dist = float('inf')

        for i, word in enumerate(wordsDict):
            if word == word1 :
                index1 = i
            elif word == word2 :
                index2 = i

            if index1 != -1 and index2 != -1 :
                min_dist = min(min_dist, abs(index1 - index2))

        return (min_dist)

s= Solution()
print(s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"))