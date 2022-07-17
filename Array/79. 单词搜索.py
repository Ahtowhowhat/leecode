from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        ans = False
        m, n = len(board), len(board[0])
        seen = [[False] * n for _ in range(m)]

        def dfs(i, j, targetIdx):
            nonlocal ans
            if i < 0 or i >= m or j < 0 or j >= n or seen[i][j] or ans:
                return
            elif board[i][j] != word[targetIdx]:
                return
            elif targetIdx == len(word) - 1:
                ans = True
                return
            seen[i][j] = True
            for dx, dy in directions:
                dfs(i + dy, j + dx, targetIdx + 1)
            seen[i][j] = False

        for i in range(m):
            for j in range(n):
                if not ans:
                    dfs(i, j, 0)
                else:
                    return ans
        return ans


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        m, n = len(board), len(board[0])
        seen = [[False] * n for _ in range(m)]

        def dfs(i, j, targetIdx):
            if i < 0 or i >= m or j < 0 or j >= n or seen[i][j]:
                return False
            elif board[i][j] != word[targetIdx]:
                return False
            elif targetIdx == len(word) - 1:
                return True
            seen[i][j] = True
            cur = False
            for dx, dy in directions:
                cur |= dfs(i + dy, j + dx, targetIdx + 1)
            seen[i][j] = False
            return cur

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False

