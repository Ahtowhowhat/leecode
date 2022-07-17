import bisect
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        return [left, right-1] if left < len(nums) and nums[left]==target else [-1, -1]