class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        stack = []

        # maintain a non increasing stack and update it when the top element is smaller than
        # current number
        for i, temp in enumerate(temperatures):
            while len(stack) and stack[-1][0] < temp:
                num, ind = stack.pop()
                ans[ind] = i - ind
            stack.append([temp,i])
        return ans

