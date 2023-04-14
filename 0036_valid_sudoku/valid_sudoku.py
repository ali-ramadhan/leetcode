def row(r, board):
    return board[r]

def col(c, board):
    return [board[r][c] for r in range(9)]

def box(n, board):
    i = n % 3
    j = n // 3
    return [board[r][c] for r in range(3*i, 3*(i+1)) for c in range(3*j, 3*(j+1))]

def valid(nums):
    nums = list(filter(lambda x: x != '.', nums))
    return len(nums) == len(set(nums))

def is_valid_sudoku(board):
    for i in range(9):
        if not valid(row(i, board)) or not valid(col(i, board)) or not valid(box(i, board)):
            return False
    return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return is_valid_sudoku(board)
