class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        ans = premax = premin = nums[0]
        for num in nums[1:]:
            premax, premin = max(num, num*premax, num*premin), min(num, premax*num, premin*num)
            ans = max(ans, premax)
        return ans