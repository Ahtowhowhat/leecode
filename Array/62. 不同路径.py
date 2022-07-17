# 62
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[m - 1][n - 1]


from functools import lru_cache


class Solution:
    @lru_cache(None)
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 1 or n <= 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)




# 63
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0]==1:
                break
            ans[i][0] = 1
        for i in range(n):
            if obstacleGrid[0][i]==1:
                break
            ans[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                ans[i][j] = (ans[i-1][j]+ans[i][j-1]) if obstacleGrid[i][j]!=1 else 0
        return ans[m-1][n-1]
