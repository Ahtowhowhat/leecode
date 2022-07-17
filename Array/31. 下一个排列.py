class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-1
        while i>0 and nums[i-1]>=nums[i]:
            i -= 1
        if i==0:
            nums.reverse()
            return
        i -= 1
        j = n-1
        while j>i and nums[j]<=nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        low = i+1
        high = n-1
        while low<high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1