from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt1 = Counter(s)
        cnt2 = Counter(t)
        return cnt2 == cnt1


from string import ascii_lowercase


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        table = dict.fromkeys(ascii_lowercase, 0)
        for c in s:
            table[c] += 1
        for c in t:
            table[c] -= 1
            if table[c] < 0:
                return False
        return True