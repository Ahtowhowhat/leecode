from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = list()
        for first in range(n):
            if first != 0 and nums[first] == nums[first - 1]:
                continue
            second, third = first + 1, n - 1
            target = -nums[first]
            while second < third:
                if second != first + 1 and nums[second] == nums[second - 1]:
                    second += 1
                    continue
                cur = nums[second] + nums[third]
                if cur == target:
                    ans.append([nums[first], nums[second], nums[third]])
                    second += 1
                elif cur > target:
                    third -= 1
                else:
                    second += 1
        return ans
