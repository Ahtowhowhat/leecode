class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        def dfs(s: str, i):
            if i<n and s[i] == '0':
                return 0

            if i == n - 1 or i == n:
                return 1
            elif i > n:
                return 0
            if s[i + 1] == '0':
                return dfs(s, i + 2)
            elif int(s[i:i + 2]) > 26:
                return dfs(s, i + 1)
            elif i + 2 < n:
                if s[i + 2] == '0':
                    return dfs(s, i + 1)
                else:
                    return dfs(s, i + 1) + dfs(s, i + 2)
            else:
                return dfs(s, i + 1) + dfs(s, i + 2)

        return dfs(s, 0)
S = Solution()
print(S.numDecodings("111111111111111111111111"))



class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        f = [1] + [0] * n
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                f[i] += f[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i-2:i]) <= 26:
                f[i] += f[i - 2]
        return f[n]
