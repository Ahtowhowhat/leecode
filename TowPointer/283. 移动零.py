class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        n = len(nums)
        while j < n:
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            j += 1
        while i < n:
            nums[i] = 0
            i += 1
