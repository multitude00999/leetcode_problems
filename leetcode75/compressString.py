class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)

        # base case
        if n == 1:
            return 1
        prev = ""
        ptr1, ptr2, temp_count, global_length = 0, 0, 0, 0

        while ptr1 < len(chars):
            ptr2 = ptr1
            # iterate until different character found
            while ptr2 < len(chars) and (prev == "" or prev == chars[ptr2]):
                prev = chars[ptr2]
                temp_count += 1
                ptr2+=1

            # set count in the target array
            count_chars = list(str(temp_count))
            chars[global_length] = prev
            if temp_count>1:
                chars[global_length+1:global_length + len(count_chars)] = count_chars
                ptr2+=1
                global_length += len(count_chars)+1
            
            else:
                global_length+=1
            
            temp_count = 0
            prev = ""
            ptr1 = ptr2
        return global_length
