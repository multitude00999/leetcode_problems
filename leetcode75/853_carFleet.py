class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        pair = sorted(pair, key = lambda x: x[0])

        stack = []
        for p in reversed(pair):
            stack.append((target - p[0])/p[1])
            # if car behind is faster make them a fleet and pop
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
