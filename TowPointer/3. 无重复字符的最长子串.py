class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        i = j = 0
        n = len(s)
        cur = set()
        while j<n:
            if s[j] not in cur:
                cur.add(s[j])
                j += 1
            else:
                cur.remove(s[i])
                i += 1
            ans = max(len(cur), ans)
        return ans