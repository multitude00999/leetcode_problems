import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = 1
        stack = []

        for i in tokens:
            if i not in '-+*/':
                stack.append(int(i))
            
            else:
                a = stack.pop()
                b = stack.pop()
                if i == '+':
                    res = a + b
                    stack.append(res)
                
                elif i =='-':
                    res = b - a
                    stack.append(res)
                
                elif i == '*':
                    res = a * b
                    stack.append(res)
                
                else:
                    res = math.trunc(b/a)
                    stack.append(res)
        return stack[-1]