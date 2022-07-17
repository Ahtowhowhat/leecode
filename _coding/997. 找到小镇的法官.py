from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n==1:
            return 1
        inmap = defaultdict(int)
        outmap = defaultdict(int)
        for a, b in trust:
            outmap[a] += 1
            inmap[b] += 1
        ans = []
        for key in inmap:
            if outmap[key]==0 and inmap[key]==n-1:
                if len(ans)==0:
                    ans.append(key)
                else:
                    return -1
        return ans[0] if len(ans) else -1

S = Solution()
print(S.findJudge(1, []))