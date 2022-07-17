from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        if max(cnt.values()) > (len(s)+1)/2:
            return ''
        queue = list(map(lambda item: (-item[1], item[0]), cnt.items()))
        heapq.heapify(queue)
        ans = []
        while len(queue) > 1:
            cnt1, char1 = heapq.heappop(queue)
            cnt2, char2 = heapq.heappop(queue)
            ans.extend([char1, char2])
            cnt1 += 1
            cnt2 += 1
            if cnt1 != 0:
                heapq.heappush(queue, (cnt1, char1))
            if cnt2 != 0:
                heapq.heappush(queue, (cnt2, char2))
        if queue:
            ans.append(queue[0][1])
        return ''.join(ans)

