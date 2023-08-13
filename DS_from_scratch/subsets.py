class Solution:
    def backtrack(self, i):
        # break condition
        if i > len(self.nums) - 1:
            self.ans.append(self.temp[:])
            return
        
        # take nums[i]
        self.temp.append(self.nums[i])
        self.backtrack(i+1)

        # do not take nums[i]
        self.temp.pop()
        self.backtrack(i+1)
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.ans = []
        self.temp = []
        self.backtrack(0)
        return self.ans
