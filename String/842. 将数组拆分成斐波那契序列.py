from typing import List
INT_MAX = 2**31-1
class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        ans = []
        n = len(num)
        ascii_zero = ord('0')
        def backTrack(i, a, b):
            if i==n:
                return len(ans)>=3
            cur = 0
            for j in range(i, n if num[i]!='0' else i+1):
                cur = cur*10+ord(num[j])-ascii_zero
                if cur>INT_MAX:
                    break
                if (a==None or b==None) or a+b==cur:
                    ans.append(cur)
                    if backTrack(j+1, b, cur):
                        return True
                    ans.pop()
                elif a+b<cur:
                    break
            return False

        backTrack(0, None, None)
        return ans

S = Solution()
print(S.splitIntoFibonacci("123456579"))