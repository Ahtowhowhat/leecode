from typing import List
from collections import Counter


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        ans = list()
        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            target = -nums[first]
            second, third = first+1,  n - 1
            while second<third:
                cur = nums[second]+nums[third]
                if cur==target:
                    ans.append([nums[first], nums[second], nums[third]])
                    third -= 1
                    while second < third and nums[third] == nums[third + 1]:
                        third -= 1
                    second += 1
                    while second < third and nums[second] == nums[second - 1]:
                        second += 1
                elif cur>target:
                    third -= 1
                    while second<third and nums[third]==nums[third+1]:
                        third -= 1
                else:
                    second += 1
                    while second<third and nums[second]==nums[second-1]:
                        second += 1
        return ans
