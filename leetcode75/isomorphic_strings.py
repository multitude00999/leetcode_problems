class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n != m:
            return False
        mapS = {}
        mapT = {}

        for i in range(n):
            if s[i] in mapS:
                if mapS[s[i]] != t[i]:
                    return False

            else:
                if t[i] in mapT:
                    return False
                mapS[s[i]] = t[i]
                mapT[t[i]] = s[i]
        return True