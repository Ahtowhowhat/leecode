class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        end = 0
        n = len(nums)
        for i in range(n):
            if end > 1 and nums[i]==nums[end-2]:
                continue
            nums[end] = nums[i]
            end += 1
        return end