class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        l = len(s)
        temp = ""
        res = ""

        # first loop for checking array length
        while i < l:
            # second loop iterates over word
            while i< l and s[i]!=' ':
                temp += s[i]
                i+=1
            if len(temp)>0:
                res+=temp + " "
            temp = ""
            i+=1
        
        # split by space and return reversed string
        arr = res.strip().split(' ')
        return " ".join(arr[::-1])
            
