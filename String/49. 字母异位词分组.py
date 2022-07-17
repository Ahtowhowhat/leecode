from collections import defaultdict
from string import ascii_lowercase
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for s in strs:
            count = dict.fromkeys(ascii_lowercase, 0)
            for c in s:
                count[c] += 1
            mp[tuple(count.values())].append(s)
        return list(mp.values())