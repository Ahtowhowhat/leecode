from typing import List



from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        delta = float('inf')
        n = len(nums)
        nums.sort()
        for first in range(n):
            if first != 0 and nums[first] == nums[first - 1]:
                continue
            cur_traget = target - nums[first]
            second, third = first + 1, n - 1
            while second < third:
                if second != first + 1 and nums[second] == nums[second - 1]:
                    second += 1
                    continue
                cur_delta = cur_traget-nums[second]-nums[third]
                delta = delta if abs(delta) < abs(cur_delta) else cur_delta
                if cur_delta>0:
                    second += 1
                elif cur_delta<0:
                    third -= 1
                else:
                    return target
        return target-delta

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = float('inf')
        n = len(nums)
        nums.sort()
        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            second, third = first + 1, n - 1
            while second < third:
                if second != first + 1 and nums[second] == nums[second - 1]:
                    second += 1
                    continue
                cur = nums[first] + nums[second] + nums[third]
                if cur == target:
                    return cur
                ans = cur if abs(cur - target) < abs(ans - target) else ans
                if cur > target:
                    third -= 1
                else:
                    second += 1
        return ans
