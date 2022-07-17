from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for i, (start, end) in enumerate(intervals):
            if start<=ans[-1][-1]:
                ans[-1][-1] = max(end, ans[-1][-1])
            else:
                ans.append([start, end])
        return ans