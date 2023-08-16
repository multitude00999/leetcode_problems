class Solution:
    def backtrack(self, n: int, k: int, temp: List[int], start: int):
        # break condition
        if n < 0 or len(temp) > k:
            return
        
        # solution found condition
        if n == 0 and len(temp) == k:
            self.ans.append(temp[:])
            return
        
        # backtrack over remaining combinations
        for i in range(start, 10):
            self.backtrack(n - i, k, temp[:] + [i], i + 1)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        self.backtrack(n, k, [], 1)
        return self.ans