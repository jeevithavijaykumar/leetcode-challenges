#36. Valid Sudoku
#Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#Each row must contain the digits 1-9 without repetition.
#Each column must contain the digits 1-9 without repetition.
#Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

import collections

class Sudoku():
    def validsudoku(self,board):
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        grid = collections.defaultdict(set)

        for r in range(0,9):
            for c in range(0,9):
                if(board[r][c]=='.'):
                    continue
                if(board[r][c] in rows[r] or
                   board[r][c] in columns[c] or
                   board[r][c] in grid[r//3,c//3]):
                    return(False)
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                grid[r//3,c//3].add(board[r][c])
            return(True)

s = Sudoku()
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(s.validsudoku(board))

