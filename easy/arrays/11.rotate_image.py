from typing import List
from math import ceil


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        n_rings = ceil(n/2)
        # Pivot by concentric rings
        for ring_i in range(0, n_rings):
            # print(f'ring {ring_i}')
            for j in range(n-2*ring_i-1):
                # print(f'j = {j}')
                # print(matrix[ring_i][ring_i+j], matrix[ring_i+j][n-1-ring_i],
                #       matrix[n-1-ring_i][n-1-ring_i-j], matrix[n-1-ring_i-j][ring_i])
                matrix[ring_i][ring_i+j], matrix[ring_i+j][n-1-ring_i], matrix[n-1-ring_i][n-1-ring_i-j], matrix[n-1-ring_i-j][ring_i] = matrix[n -
                                                                                                                                                1-ring_i-j][ring_i], matrix[ring_i][ring_i+j], matrix[ring_i+j][n-1-ring_i], matrix[n-1-ring_i][n-1-ring_i-j]


if __name__ == "__main__":
    matrix = [[2, 29, 20, 26, 16, 28],
              [12, 27, 9, 25, 13, 21],
              [32, 33, 32, 2, 28, 14],
              [13, 14, 32, 27, 22, 26],
              [33, 1, 20, 7, 21, 7],
              [4, 24, 1, 6, 32, 34]]
    Solution().rotate(matrix)
    print(matrix)
