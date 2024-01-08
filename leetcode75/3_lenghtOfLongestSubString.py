class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hashmap for traicking seen element by storing last seen index
        hashmap = {}
        sub_start = 0
        res = 0
        
        # iterate
        for i, char in enumerate(s):

            # if char already seen restart substring
            if hashmap.get(char, -1) >= sub_start:
                sub_start = hashmap.get(char, -1) + 1
            hashmap[char] = i
            res = max(res, i - sub_start + 1)
        return res
