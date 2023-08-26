class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        
        # use swapping to save memory
        prev, prev2 = 0, 1
        for i in range(2, n+2):
            curr = prev + prev2
            prev2 = prev
            prev = curr
        return prev

class Solution:
    def fibCalculate(self, n):

        # check if solution already exists
        if self.dp[n] != -1:
            return self.dp[n]
        
        # otherwise get the solution
        self.dp[n] = self.fibCalculate(n-1) + self.fibCalculate(n-2)
        return self.dp[n]
    def fib(self, n: int) -> int:

        # base case
        if n <=1:
            return n
        # intitialize dp array for storing subproblem solutions
        self.dp = [-1]*(n+1)

        # initialize solution for base cases
        self.dp[0], self.dp[1] = 0, 1

        return self.fibCalculate(n)

