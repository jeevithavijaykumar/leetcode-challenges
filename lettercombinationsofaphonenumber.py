#17. Letter Combinations of a Phone Number
#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
#Return the answer in any order.

class Phonenumber():
    def lettercombinations(self,digits):
        res =[]
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def backtracking(i,curstr):
            if(len(curstr)==len(digits)):
                res.append(curstr)
                return
            for c in d[digits[i]]:
                backtracking(i+1,curstr+c)

        if(digits):
            backtracking(0,'')
        return(res)

p = Phonenumber()
print(p.lettercombinations('23'))
