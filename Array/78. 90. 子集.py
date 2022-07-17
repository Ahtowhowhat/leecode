# 78. 子集
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        cur = []
        n = len(nums)

        def dfs(i):
            if i == n:
                ans.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()
            dfs(i + 1)

        dfs(0)
        return ans


# 90. 子集 II
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        ans = set()
        cur = []
        n = len(nums)

        def dfs(i):
            if i == n:
                ans.add(tuple(sorted(cur)))
                return
            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()
            dfs(i + 1)

        dfs(0)
        ans = list(map(list, ans))
        return ans


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        ans = []
        cur = []
        n = len(nums)

        def dfs(i, choosePre):
            if i == n:
                ans.append(cur.copy())
                return
            dfs(i + 1, False)
            if not choosePre and i > 0 and nums[i] == nums[i - 1]:
                return
            cur.append(nums[i])
            dfs(i + 1, True)
            cur.pop()

        nums.sort()
        dfs(0, False)
        return ans
