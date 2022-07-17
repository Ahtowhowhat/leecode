# 54
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m, n = len(matrix), len(matrix[0])
        numoflayer = (min(m, n) + 1) // 2
        ans = []
        for layer in range(numoflayer):
            left_top = (layer, layer)
            right_top = (layer, n - 1 - layer)
            right_bottom = (m - 1 - layer, n - 1 - layer)
            left_bottom = (m - 1 - layer, layer)
            if left_top == left_bottom:
                i = left_top[0]
                for j in range(left_top[1], right_top[1]):
                    ans.append(matrix[i][j])
                ans.append(matrix[right_top[0]][right_top[1]])
                break
            if left_top == right_top:
                j = right_top[1]
                for i in range(right_top[0], right_bottom[0]):
                    ans.append(matrix[i][j])
                ans.append(matrix[right_bottom[0]][right_bottom[1]])
                break
            i = left_top[0]
            for j in range(left_top[1], right_top[1]):
                ans.append(matrix[i][j])
            j = right_top[1]
            for i in range(right_top[0], right_bottom[0]):
                ans.append(matrix[i][j])
            i = right_bottom[0]
            for j in range(right_bottom[1], left_bottom[1], -1):
                ans.append(matrix[i][j])
            j = left_bottom[1]
            for i in range(left_bottom[0], left_top[0], -1):
                ans.append(matrix[i][j])
        return ans


# 54
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        i = j = 0
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        dirIdx = 0
        ans = []
        cnt = 0
        m, n = len(matrix), len(matrix[0])
        while cnt < m * n:
            ans.append(matrix[i][j])
            matrix[i][j] = None
            new_i = i + directions[dirIdx][0]
            new_j = j + directions[dirIdx][1]
            if new_i >= m or new_i < 0 or new_j >= n or new_j < 0 or matrix[new_i][new_j] is None:
                dirIdx = (dirIdx + 1) % 4
                new_i = i + directions[dirIdx][0]
                new_j = j + directions[dirIdx][1]
            i, j = new_i, new_j
            cnt += 1
        return ans


# 59
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        i = j = 0
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        dirIdx = 0
        x = 1
        while x <= n * n:
            matrix[i][j] = x
            new_i = i + directions[dirIdx][0]
            new_j = j + directions[dirIdx][1]
            if new_i >= n or new_i < 0 or new_j >= n or new_j < 0 or matrix[new_i][new_j] != 0:
                dirIdx = (dirIdx + 1) % 4
                new_i = i + directions[dirIdx][0]
                new_j = j + directions[dirIdx][1]
            i, j = new_i, new_j
            x += 1
        return matrix
