class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        if n < m:
            return ""
        t_hashmap = Counter(t)
        t_keys = len(t_hashmap)

        s_hashmap = Counter()
        matches = 0
        answer = ""
        l, r = 0, -1

        while l < len(s):
            if matches < t_keys:

                # break condition
                if r == len(s) -  1:
                    return answer
                # extend
                r += 1
                s_hashmap[s[r]] += 1
                if t_hashmap[s[r]] > 0 and s_hashmap[s[r]] == t_hashmap[s[r]]:
                    matches += 1
            
            else:
                # contract
                s_hashmap[s[l]] -= 1
                if t_hashmap[s[l]] > 0 and s_hashmap[s[l]] + 1 == t_hashmap[s[l]]:
                    matches -= 1
                l += 1
            
            # check if valid substring found
            if matches == t_keys:
                if answer == "":
                    answer = s[l:r+1]
                elif len(answer) > r - l + 1:
                    answer = s[l:r+1]
        return answer