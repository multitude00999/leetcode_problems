class Solution:
    def backtrack(self, target: int, temp: List[int], start: int):
        if target < 0:
            return
            
        elif target == 0:
            self.ans.append(temp[:])
            return
        
        for i in range(start, self.n):
            # take one element only once
            if i > start and self.candidates[i] == self.candidates[i-1]:
                continue
            self.backtrack(target - self.candidates[i], temp[:] + [self.candidates[i]], i + 1)


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.candidates = candidates
        self.candidates.sort()
        self.n = len(self.candidates)
        self.ans = []
        self.backtrack(target, [], 0)
        return self.ans