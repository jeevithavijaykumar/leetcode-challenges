""" 6. Zigzag conversion"""
"""The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:"""

class Solution():
    def zigzagconversion(self,s,numRows):
        if(numRows==1 or numRows>=len(s)):
            return(s)
        index=0
        direction=1
        rows = [[] for i in range(numRows)]
        for char in s:
            rows[index].append(char)
            if(index==0):
                direction=1
            elif(index==numRows-1):
                direction=-1
            index=index+direction
        for j in range(numRows):
            rows[j]="".join(rows[j])

        return("".join(rows))

s=Solution()
print(s.zigzagconversion("PAYPALISHIRING",4))