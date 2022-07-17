from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        pre = [float('inf')] * (len(triangle[-1])+1)
        pre[1] = triangle[0][0]
        layers = len(triangle)
        for layer in range(1, layers):
            cur = pre.copy()
            for i in range(len(triangle[layer])):
                cur[i+1] = min(pre[i], pre[i+1])+triangle[layer][i]
            pre = cur
        return min(pre)


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        pre_cur = [[float('inf')] * (len(triangle[-1])+1) for _ in range(2)]
        pre_cur[0][1] = triangle[0][0]
        layers = len(triangle)
        for layer in range(1, layers):
            cur, pre = layer%2, 1-layer%2
            for i in range(len(triangle[layer])):
                pre_cur[cur][i+1] = min(pre_cur[pre][i], pre_cur[pre][i+1])+triangle[layer][i]
        return min(pre_cur[(layers-1)%2])