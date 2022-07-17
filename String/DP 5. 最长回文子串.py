class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, max_l = 0, 1
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for l in range(2, n+1):
            for i in range(n):
                j = i+l-1
                if j>=n:
                    break
                if j==i+1:
                    dp[i][j] = s[i]==s[j]
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i]==s[j]
                if dp[i][j] and l>max_l:
                    start = i
                    max_l = l
        return s[start:start+max_l]
