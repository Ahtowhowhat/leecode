# 贪心（1026 / 1306）
"""
输入：
"abcdxabcde"
"abcdeabcdx"
输出：
10
预期结果：
4
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def func(word1: str, word2: str) -> int:
            i = j = 0
            step = 0
            for i in range(len(word1)):
                t = j
                while t < len(word2) and word2[t] != word1[i]:
                    t += 1
                j = t + 1 if t < len(word2) else j
                if t == len(word2):
                    step += 1
            return step + len(word2) - (len(word1) - step)

        return min(func(word1, word2), func(word2, word1))


# 动态规划
# 类似题目 DP 1143. 最长公共子序列.py

def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1) + 1, len(text2) + 1
    dp = [[0] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m - 1][n - 1]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        LCS = longestCommonSubsequence(word1, word2)
        return len(word1)+len(word2)-2*LCS
