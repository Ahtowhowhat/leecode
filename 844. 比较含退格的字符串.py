class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def nextch(s: str, i):
            skip = 0
            while i>=0:
                if s[i]=='#':
                    skip += 1
                else:
                    if skip>0:
                        skip -= 1
                    else:
                        yield s[i]
                i -= 1
            yield None
        getS, getT = nextch(S, len(S)-1), nextch(T, len(T)-1)
        while True:
            s, t = next(getS), next(getT)
            if s!=t:
                return False
            if s is None and t is None:
                return True

