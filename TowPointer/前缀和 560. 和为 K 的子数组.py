class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        mp = {0: 1}
        ans = 0
        cur = 0
        for i in range(len(nums)):
            cur += nums[i]
            ans += mp.get(cur - k, 0)
            mp[cur] = mp.get(cur, 0) + 1
        return ans
