from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def mysort(low, high, x):
            nonlocal nums
            while low<high:
                while low<high and nums[low]==x:
                    low += 1
                while low<high and nums[high]!=x:
                    high -= 1
                nums[low], nums[high] = nums[high], nums[low]
            return low
        n = len(nums)
        mysort(mysort(0, n-1, 0), n-1, 1)
