class Solution:
    def backtrack(self, target: int, temp: List[int], start: int):
        # if current sum of target is greater than target then break since we've only positive integers
        if target < 0:
            return
        
        # if target achieved. add it to ans if not already added
        elif target == 0:
            self.ans.append(temp[:])
            return
        
        # backtrack
        for i in range(start, self.n):
            self.backtrack(target - self.candidates[i], temp + [self.candidates[i]], i)


        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.n = len(candidates)
        self.candidates = candidates
        self.backtrack(target, [], 0)
        return self.ans