class Solution:
    def maxSubArrayLen(self, nums: list[int], k: int):
        mp = {0: -1}
        ans = 0
        cur = 0
        for idx, num in enumerate(nums):
            cur += num
            if cur - k in mp:
                ans = max(ans, idx - mp[cur - k])
            if cur not in mp:
                mp[cur] = idx
        return ans
