class Solution:
    def backtrack(self, i, temp):

        # break condition
        if i > len(self.digits) -1:
            self.ans.append(temp[:])
            return 
        
        # backtrack
        for char in self.mapping[int(self.digits[i])]:
            self.backtrack(i + 1, temp + char)


    def letterCombinations(self, digits: str) -> List[str]:
        # map digits to characters
        self.mapping = {2:'abc',
                    3: 'def',
                    4: 'ghi',
                    5: 'jkl',
                    6: 'mno',
                    7: 'pqrs',
                    8: 'tuv', 
                    9: 'wxyz'}

        # backtrack
        self.ans = []
        self.digits = digits
        self.backtrack(0, "")
        if len(self.digits) == 0:
            return []
        return self.anss