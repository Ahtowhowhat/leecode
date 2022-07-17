from typing import List

# 39
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        total = 0
        n = len(candidates)
        def dfs(idx):
            nonlocal total
            if total == target:
                ans.append(cur.copy())
                return
            elif total > target:
                return
            for i in range(idx, n):
                total += candidates[i]
                cur.append(candidates[i])
                dfs(i)
                total -= candidates[i]
                cur.pop()

        dfs(0)
        return ans

# 40
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        total = 0
        n = len(candidates)
        candidates.sort()
        def dfs(idx):
            nonlocal total
            if total == target:
                ans.append(cur.copy())
                return
            elif total > target:
                return
            for i in range(idx, n):
                # 在39的基础上加入一步判断，防止当前位置使用重复数字即可，此判断
                if i!=idx and candidates[i]==candidates[i-1]:
                    continue
                total += candidates[i]
                cur.append(candidates[i])
                dfs(i+1)
                total -= candidates[i]
                cur.pop()

        dfs(0)
        return ans