class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        pre = 0
        cur = nums[0]
        ans = nums[0]
        for i, num in enumerate(nums):
            cur = max(pre+num, num)
            pre = cur
            ans = max(ans, cur)
        return ans