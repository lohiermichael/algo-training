from typing import List


class Solution:
    def hasDuplicates(self, l: List['str']):
        l_copy = [item for item in l if item != '.']
        return len(l_copy) != len(set(l_copy))

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check the rows (9)
        for row in range(9):
            if self.hasDuplicates(board[row]):
                return False

        # Check the columns (9)
        for column in range(9):
            if self.hasDuplicates([row[column] for row in board]):
                return False

        # Check the boxes (9)
        for k1 in range(3):
            for k2 in range(3):
                if self.hasDuplicates([board[3*k1 + r1][3*k2+r2]
                                       for r1 in range(3)
                                       for r2 in range(3)]):
                    return False

        return True


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
print(Solution().isValidSudoku(board))
