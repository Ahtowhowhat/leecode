class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = [0]
        i, n = 0, len(s)
        for i in range(n):
            if s[i]=='(':
                stk.append(0)
            else:
                score = max(stk.pop()*2, 1)
                stk[-1] += score
        return stk.pop()

