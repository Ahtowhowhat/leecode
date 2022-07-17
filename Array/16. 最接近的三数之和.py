from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = float('inf')
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            a = nums[i]
            # t = target-a
            j, k = i + 1, n - 1
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                while j < k:
                    cur = nums[i] + nums[j] + nums[k]
                    if cur < target:
                        ans = cur if abs(cur - target) < abs(ans - target) else ans
                        break
                    elif cur == target:
                        return cur
                    k -= 1
                    ans = cur if abs(cur - target) < abs(ans - target) else ans
        return ans



class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = float('inf')
        for first in range(n):
            if first>0 and nums[first]==nums[first-1]:
                continue
            second, third = first+1, n-1
            while second<third:
                cur = nums[first]+nums[second]+nums[third]
                if cur==target:
                    return cur
                ans = cur if abs(cur-target)<abs(ans-target) else ans
                if cur>target:
                    third -= 1
                    while third>second and nums[third]==nums[third+1]:
                        third -= 1
                else:
                    second += 1
                    while second<third and nums[second]==nums[second-1]:
                        second += 1
        return ans