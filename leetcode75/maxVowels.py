class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        temp_count = 0
        max_count = 0
        vowels = "aeiou"

        # calculate number of vowels in substring of size k starting at index 0
        for i in s[:k]:
            if i in vowels:
                temp_count+=1
        max_count = max(max_count, temp_count)

        # iterate over rest of the array and keep updating max number of vowels
        for i in range(1, n-k+1):
            if s[i-1] in vowels:
                temp_count-=1
            if s[i+k-1] in vowels:
                temp_count+=1
            max_count = max(temp_count, max_count)
            
        return max_count
