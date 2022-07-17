from typing import List
# 法一 时间复杂度O（mn） 空间复杂度O（m+n）
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows, cols = [1] * m,  [1]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    rows[i] = cols[j] = 0
        for i in range(m):
            for j in range(n):
                if rows[i]==0 or cols[j]==0:
                    matrix[i][j] = 0

# 法二 时间复杂度O（mn） 空间复杂度O（1）
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row0 = any((matrix[0][j]==0 for j in range(n)))
        col0 = any(matrix[i][0]==0 for i in range(m))
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j]==0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j] = 0
        if row0:
            for j in range(n):
                matrix[0][j] = 0
        if col0:
            for i in range(m):
                matrix[i][0] = 0