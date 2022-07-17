from typing import List

# 26. 删除有序数组中的重复项
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for num in nums:
            if num != nums[index]:
                index += 1
                nums[index] = num
        return index + 1

# 80. 删除有序数组中的重复项 II
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i] or i == 0 or nums[j] != nums[i - 1]:
                i += 1
                nums[i] = nums[j]
        return i + 1