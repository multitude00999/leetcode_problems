class Solution1:
    def climbStairs(self, n: int) -> int:
        # base case
        if n <=1:
            return 1
        
        # fibonacci solution with o(1) memory
        prev, prev2 = 1, 1
        for i in range(2, n+1):
            curr = prev + prev2
            prev2 = prev
            prev = curr
        
        return prev 

class Solution2:
    def climbStairs(self, n: int) -> int:
        # base case
        if n <=1:
            return 1
        
        # dp solution
        dp = [-1]*(n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]