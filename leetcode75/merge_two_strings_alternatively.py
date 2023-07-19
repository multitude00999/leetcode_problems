class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        shorter = n if n < m else m
        i, j = 0, 0
        global_itr = 0
        res = ""
        while(global_itr < shorter*2):
            if global_itr%2 == 0:
                res += word1[i]
                i+=1
            else:
                res += word2[j]
                j+=1
            global_itr+=1
        if shorter == n:
            res += word2[shorter:]
        
        else:
            res+=word1[shorter:]

        return res