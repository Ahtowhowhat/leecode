# 55.跳跃游戏
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        longest = 0
        for i, num in enumerate(nums):
            if i > longest:
                return False
            longest = max(i + num, longest)
        return longest >= len(nums) - 1

# 45. 跳跃游戏 II
class Solution:
    def jump(self, nums: list[int]) -> int:
        step = 0
        end = len(nums)-1
        longest = nums[0]  # 走完step+1步后，能到达的最远位置
        curEnd = 0  # 走完step步后，能到的最远位置
        for i, num in enumerate(nums[:-1]):
            if i<=curEnd:
                longest = max(i + num, longest)
                if i==curEnd:
                    step += 1
                    curEnd = longest
        return step


class Solution:
    def jump(self, nums: list[int]) -> int:
        step = 0
        end = len(nums)-1
        longest = nums[0]  # 走完step步后，再走一步，能到达的最远位置
        curEnd = 0  # 走完step步后，能到的最远位置
        if curEnd >= end:
            return step
        for i, num in enumerate(nums):
            if i<=curEnd:
                longest = max(i + num, longest)
                if i==curEnd:
                    step = step+1
                    curEnd = longest
                    if curEnd>=end:
                        return step
        return None

