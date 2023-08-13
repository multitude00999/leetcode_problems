class Solution:
    def backtrack(self):
        # check if temp is of required length
        if len(self.temp) == len(self.nums):
            self.ans.append(self.temp[:])
            return
        
        # recursively backtrack over all permutations
        for a in self.nums:
            if a not in self.temp:
                self.temp.append(a)
                self.backtrack()
                self.temp.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.ans = []
        self.temp = []
        self.backtrack()
        return self.ans