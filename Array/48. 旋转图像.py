from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def T(matrix: matrix):
            n = len(matrix)
            for i in range(n):
                for j in range(i, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        def lrconvert(matrix: matrix):
            n = len(matrix)
            for i in range(n):
                left, right = 0, n-1
                while left<right:
                    matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                    left += 1
                    right -=1
        T(matrix)
        lrconvert(matrix)