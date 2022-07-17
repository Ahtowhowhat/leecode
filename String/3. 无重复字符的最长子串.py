class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = set()
        ans = 0
        i, j = 0, 0
        n = len(s)
        while j<n:
            if s[j] not in cur:
                cur.add(s[j])
                j += 1
            else:
                cur.remove(s[i])
                i += 1
            ans = max(ans, j-i)
        return ans
