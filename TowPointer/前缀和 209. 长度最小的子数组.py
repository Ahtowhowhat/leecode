# 滑动窗口
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        cur = -target
        i = j = 0
        n = len(nums)
        ans = n + 1
        while j < n:
            if cur < 0:
                cur += nums[j]
                j += 1
            else:
                cur -= nums[i]
                i += 1
            if cur >= 0:
                ans = j - i if ans is None else min(ans, j - i)
        while i < j:
            cur -= nums[i]
            i += 1
            if cur >= 0:
                ans = min(ans, j - i)
            else:
                break
        return ans if ans != n + 1 else 0


# 前缀和
import bisect


class Solution:
    def minSubArrayLen(self, s: int, nums: list[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + nums[i])

        for i in range(1, n + 1):
            target = s + sums[i - 1]
            bound = bisect.bisect_left(sums, target)
            if bound != len(sums):
                ans = min(ans, bound - (i - 1))

        return 0 if ans == n + 1 else ans
