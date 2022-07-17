class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        end = len(s)
        ans = list()
        cur = list()
        def backtrack(n, begin):
            if begin>=end:
                return
            if n==4:
                num = int(s[begin:end])
                if begin<end and num<256:
                    if end-begin>1 and s[begin]=='0':
                        return
                    else:
                        ans.append('.'.join(cur)+'.'+s[begin:end])
                else:
                    return
            offset = 2 if s[begin]=='0' else 4
            for i in range(begin+1, begin+offset):
                num = int(s[begin:i])
                if num<256:
                    cur.append(s[begin:i])
                    backtrack(n+1, i)
                    cur.pop()
        backtrack(1, 0)
        return ans