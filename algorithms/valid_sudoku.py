"""
36. Valid Sudoku

Need to validate Sudoku

Example:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
"""

import numpy as np
class Solution(object):
                
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        valid = np.zeros(len(board) + 1)
        for row in board:
            for i in range(len(row)):
                  if ord(row[i]) in range(49, 58):
                    if valid[int(row[i])] == 0:
                        valid[int(row[i])] = 1
                    else:
                         return False
            valid = np.zeros(len(board) + 1)
            
            
        valid = np.zeros(len(board) + 1)
        for i in range(len(board)):
            for j in range(len(board)):
                if ord(board[j][i]) in range(49, 58):
                    if valid[int(board[j][i])] == 0:
                        valid[int(board[j][i])] = 1
                    else:
                        return False
            valid = np.zeros(len(board) + 1)
        
        valid = np.zeros(len(board) + 1)
        for i in range(3):
            for j in range(3):
                for i1 in range(i * 3 - 3, i * 3):
                    for j1 in range(j * 3 - 3, j * 3):
                        if ord(board[i1][j1]) in range(49, 58):
                            if valid[int(board[i1][j1])] == 0:
                                valid[int(board[i1][j1])] = 1
                            else:
                                return False
                valid = np.zeros(len(board) + 1)
        return True
        
        