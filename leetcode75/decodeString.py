class Solution:
    def decodeString(self, s: str) -> str:

        # stack to store ["final string" , rep_count, "curr_string"], initialize final string to ""
        answer_stack = []
        ans_string, count = "", 0
        answer_stack.append(ans_string)
        
        for char in s:
            # calculate repititions if the character is numeric
            if char.isnumeric():
                count = count*10 + int(char)

            # if char is '[', means ending of repition number, and add "" for curr_string
            elif char == '[':
                answer_stack.append(count)
                answer_stack.append("")

                # reset repition counter
                count = 0

            # if char is ']' means ending of string to be repeated
            elif char == ']':
                curr_string = answer_stack.pop()
                count = answer_stack.pop()

                # multiply the current string and add to final string
                answer_stack[-1] += count*curr_string

                # reset repition counter
                count = 0
            else:

                # concat to curr_string
                answer_stack[-1] += char

        return "".join(answer_stack[-1])