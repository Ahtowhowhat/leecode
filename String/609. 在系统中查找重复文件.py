from typing import List
from collections import defaultdict
import re
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        p = re.compile(r'(.+)\((.*)\)')
        hashtable = defaultdict(list)
        for dir_file in paths:
            dir_file = dir_file.split()
            directory = dir_file[0]
            files = dir_file[1:]
            for file in files:
                filename, content = p.match(file).groups()
                hashtable[content].append(directory+'/'+filename)
        return [lst for lst in hashtable.values() if len(lst)>1]