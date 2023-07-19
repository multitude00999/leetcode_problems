class Solution:
    def reverseVowels(self, s: str) -> str:
        l = len(s)
        res = list(s)

        # left and right pointer
        start_ptr, end_ptr = 0, l - 1

        # vowel list
        vowels = ['a', 'e', 'i', 'o', 'u' , 'A', 'E', 'I', 'O', 'U']
        while start_ptr < end_ptr:
            # move pointer until both pointer have value as a vowel
            if s[start_ptr] not in vowels:
                start_ptr+=1
            
            if s[end_ptr] not in vowels:
                end_ptr-=1
            
            # swap the two pointer values is ther are both vowels
            if s[start_ptr] in vowels and s[end_ptr] in vowels:
                res[start_ptr], res[end_ptr] = res[end_ptr], res[start_ptr]
                start_ptr+=1
                end_ptr-=1
        return "".join(res)
            