class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        i, j = 0, 0
        n, m = len(str1), len(str2)
        shorter = min(n,m)

        for i in range(shorter, 0 , -1):
            # check if length are divisible and we can reconstruct both strings
            if n%i == 0 and m%i == 0 and str1[:i]*(n//i) == str1 and str1[:i]*(m//i) == str2:
                return str1[:i]
        return ""


