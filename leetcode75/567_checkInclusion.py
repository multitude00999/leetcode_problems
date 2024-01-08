class Solution:
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)

        # base case
        if n > m:
            return False
        # hashmap for string 2
        hashmap = {key: 0 for key in range(26)}
        for char in s1:
            hashmap[ord(char) - ord('a')] += 1
        
        # sliding window hashmap
        temp_hashmap = {key: 0 for key in range(26)}
        for i in range(n):
            temp_hashmap[ord(s2[i]) - ord('a')] += 1
        
        if temp_hashmap == hashmap:
            return True
        
        for j in range(n, m):
            temp_hashmap[ord(s2[j-n]) - ord('a')] -= 1
            temp_hashmap[ord(s2[j]) - ord('a')] += 1

            if temp_hashmap == hashmap:
                return True
        if temp_hashmap == hashmap:
            return True
        return False 