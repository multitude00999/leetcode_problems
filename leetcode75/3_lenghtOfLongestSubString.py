class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hasmap = set()
        i = 0
        n = len(s)
        ans = 0
        hashmap = set()
        count = 0
        while i < n:
            j = i
            while j < n and s[j] not in hashmap:
                count += 1
                hashmap.add(s[j])
                j += 1
            ans = max(ans, count)
            hashmap.remove(s[i])
            i = j + 1
        return ans
