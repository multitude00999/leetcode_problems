class Solution:
    def backtrack(self, count_open_par, count_close_par, temp):
        # exit condition
        # if string has n pairs of well formed parenthesis
        if len(temp) == 2*self.n:
            self.ans.append(temp[:])
            return
        
        # if there are open parenthesis available
        if count_open_par < self.n:
            self.backtrack(count_open_par + 1, count_close_par, temp + '(')
        
        # make sure that the added closed paranthesis is well formed
        if count_close_par < count_open_par:
            self.backtrack(count_open_par, count_close_par + 1, temp + ')')

    def generateParenthesis(self, n: int) -> List[str]:
        # keep count of open and closed parenthesis
        count_open_par, count_close_par = 0, 0

        self.n = n
        self.ans = []
        self.backtrack(count_open_par, count_close_par, "")
        return self.ans