class Solution:
    def tribonacci(self, n: int) -> int:
        if n <=1:
            return n
        elif n == 2:
            return 1
        prev3, prev2, prev = 0, 1, 1
        for i in range(3, n+1):
            curr = prev + prev2 + prev3
            prev3 = prev2
            prev2 = prev
            prev = curr
        return prev