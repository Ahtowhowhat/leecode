class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        n = len(path)
        i = 0
        while i<n:
            if path[i]=='/':
                i += 1
            else:
                j = i+1
                while j<n and path[j]!='/':
                    j += 1
                name = path[i:j]
                i = j
                if name=='.':
                    continue
                elif name=='..':
                    if len(ans)>0:
                        ans.pop()
                else:
                    ans.append(name)
        print(ans)
        return '/'+'/'.join(ans)

S = Solution()
S.simplifyPath("/../")