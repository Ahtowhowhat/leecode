from typing import List
import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = bisect.bisect_left([matrix[i][0] for i in range(len(matrix))], target)
        if row<len(matrix) and matrix[row][0]==target:
            return True
        elif row==0:
            return False
        else:
            row -= 1
        col = bisect.bisect_left(matrix[row], target)
        if col== len(matrix[0]):
            return False
        return matrix[row][col]==target

s = Solution()
s.searchMatrix([[1]], 2)

# 240. 搜索二维矩阵 II
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1
        while i<m and j>=0:
            if matrix[i][j]<target:
                i += 1
            elif matrix[i][j]>target:
                j -= 1
            else:
                return True
        return False