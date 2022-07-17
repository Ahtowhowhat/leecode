class Solution:
    MAP = {'2': 'abc',
           '3': 'def',
           '4': 'ghi',
           '5': 'jkl',
           '6': 'mno',
           '7': 'pqrs',
           '8': 'tuv',
           '9': 'wxyz'}

    def letterCombinations(self, digits: str) -> list[str]:
        ans = []
        cur = []
        n = len(digits)
        if n == 0:
            return ans

        def dfs(i):
            if i == n:
                ans.append(''.join(cur))
                return
            for c in Solution.MAP[digits[i]]:
                cur.append(c)
                dfs(i + 1)
                cur.pop()

        dfs(0)
        return ans
