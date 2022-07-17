class Solution:
    def expandAroundCenter(self, s, left, right):
        cnt = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            cnt += 1
            left -= 1
            right += 1
        return cnt

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            ans += self.expandAroundCenter(s, i, i)
            ans += self.expandAroundCenter(s, i, i+1)
        return ans


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(2*n-1):
            left, right = i//2, i//2+i%2
            while left>=0 and right<n and s[left]==s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans



# 也可用动态规划
