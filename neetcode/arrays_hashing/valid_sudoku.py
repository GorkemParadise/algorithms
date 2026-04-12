"""
Problem: Valid Sudoku
Link: https://neetcode.io/problems/valid-sudoku/question?list=neetcode150
Difficulty: Medium
"""
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in s:
                    return False
                s.add(board[i][j])

        for j in range(9):
            s = set()
            for i in range(9):
                if board[i][j] != "." and board[i][j] in s:
                    return False
                s.add(board[i][j])

        for i in range(3):
            for j in range(3):
                s = set()
                for k in range(3):
                    for l in range(3):
                        if board[i*3+k][j*3+l] != "." and board[i*3+k][j*3+l] in s:
                            return False
                        s.add(board[i*3+k][j*3+l])
        return True

# Algoritmanın mantığı: Tahtayı gezdik sayı olanları bir sete ekliyoruz. Eğer aynı sayı tekrar gelirse, bu sudoku geçersizdir. 
# Bu işlemi satırlar, sütunlar ve 3x3 alt kutular için yapıyoruz.






board1 = [
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","8",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
]


board2 = [
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","1",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
]