class Solution:
    def maxArea(self, height: list[int]) -> int:
        i, j = 0, len(height)-1
        ans = 0
        while i<j:
            ans = max(ans, (j-i)*min(height[i], height[j]))
            if height[i]>height[j]:
                j -= 1
            else:
                i += 1
        return ans