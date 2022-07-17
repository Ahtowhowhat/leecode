import re
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cnt = list(map(lambda x: len(x[0]), re.findall(r'((.)\2*)', s)))
        return sum([min(cnt[i], cnt[i+1]) for i in range(len(cnt)-1)])


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cnt = []
        n = len(s)
        i = j = 0
        while i<n:
            c = s[i]
            t = 0
            while i<n and s[i]==c:
                i += 1
                t += 1
            cnt.append(t)
        return sum([min(cnt[i], cnt[i + 1]) for i in range(len(cnt) - 1)])
