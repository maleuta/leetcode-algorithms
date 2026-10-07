from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        hash_rows = defaultdict(set)
        hash_cols = defaultdict(set)
        hash_squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in hash_cols[c] or
                    board[r][c] in hash_rows[r] or
                    board[r][c] in hash_squares[r// 3 * 3 + c // 3]):
                    return False
                
                else:
                    hash_cols[c].add(board[r][c])
                    hash_rows[r].add(board[r][c])
                    hash_squares[r// 3 * 3 + c // 3].add(board[r][c])

        return True

board=[["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(Solution().isValidSudoku(board))