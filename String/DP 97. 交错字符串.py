class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False
        f = [[False for j in range(len(s2)+1)] for i in range(len(s1)+1)]
        f[0][0] = True
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                p = i+j
                if i>0:
                    f[i][j] = (f[i-1][j] and s1[i-1]==s3[p-1])
                if j>0:
                    f[i][j] |= (f[i][j-1] and s2[j-1]==s3[p-1])
        return f[len(s1)][len(s2)]


# 滚动数组优化空间复杂度
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False
        f = [False for j in range(len(s2)+1)]
        f[0] = True
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                p = i+j
                if i>0:
                    f[j] = (f[j] and s1[i-1]==s3[p-1])
                if j>0:
                    f[j] |= (f[j-1] and s2[j-1]==s3[p-1])
        return f[len(s2)]