from typing import List
import collections


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        for row in range(9):
            for column in range(9):
                if board[row][column] != ".":
                    if (
                        board[row][column] in rows[row]
                        or board[row][column] in cols[column]
                        or board[row][column] in squares[(row // 3, column // 3)]
                    ):
                        return False
                    else:
                        cols[column].add(board[row][column])
                        rows[row].add(board[row][column])
                        squares[(row // 3, column // 3)].add(board[row][column])
        return True


bruh = Solution()
print(
    bruh.isValidSudoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
