class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n != m:
            return False
        countCharS = {}
        countCharT = {}

        for i in range(n):
            if s[i] in countCharS:
                countCharS[s[i]] += 1 
            else:
                countCharS[s[i]] = 1 
            
            if t[i] in countCharT:
                countCharT[t[i]] += 1 

            else:
                countCharT[t[i]] = 1

        s_sh = ""
        t_sh = ""
        for i in range(n):
            if countCharS[s[i]] !=  countCharT[t[i]]:
                return False
            if len(s_sh)==0 or s_sh[-1]!=s[i] :
                s_sh+=s[i]
            if len(t_sh)==0 or t_sh[-1]!=t[i]:
                t_sh+=t[i]
        if len(s_sh)!=len(t_sh):
            return False
        return True

        