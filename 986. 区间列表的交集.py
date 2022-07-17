from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0
        while i< len(firstList) and j< len(secondList):
            starti, endi = firstList[i]
            startj, endj = secondList[j]
            if endi<startj:
                i += 1
            elif endj<starti:
                j += 1
            else:
                start = max(starti, startj)
                end = min(endi, endj)
                ans.append([start, end])
                if endj>endi:
                    i += 1
                else:
                    j += 1
        return ans