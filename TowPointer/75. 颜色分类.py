class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = j = k = 0
        while k<n:
            if nums[k]==0:
                nums[i], nums[k] = nums[k], nums[i]
                if i!=j:
                    nums[j], nums[k] = nums[k], nums[j]
                i += 1
                j += 1
            elif nums[k]==1:
                nums[j], nums[k] = nums[k], nums[j]
                j += 1
            k += 1

