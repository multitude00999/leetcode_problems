class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if len(stack) == 0:
                stack.append(i)
            
            # check for the closed bracket
            elif stack[-1] == '(' and i == ')':
                stack.pop()
            
            # check for the square bracket
            elif stack[-1] == '[' and i == ']':
                    stack.pop()
            
            # check for the curly bracket
            elif stack[-1] == '{' and i == '}':
                    stack.pop()
                
            else:
                stack.append(i)
        
        return len(stack) == 0
