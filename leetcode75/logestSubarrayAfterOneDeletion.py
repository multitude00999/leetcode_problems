class Solution1:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        # base cases
        if n < 2:
            return 0

        # initialize two pointers at the starting of the array
        left_ptr, right_ptr, num_zeroes = 0, 0, 0
        max_length, curr_length = 0, 0

        # move right pointer for iterating over the array
        for right_ptr in range(n):
            if nums[right_ptr] == 0:
                num_zeroes += 1
            
            # move left pointer until there is only one zero in the subarray
            while left_ptr < n and num_zeroes > 1:
                if nums[left_ptr] == 0:
                    num_zeroes -= 1
                left_ptr += 1
            curr_length = right_ptr - left_ptr + 1
            max_length = max(max_length, curr_length - 1)

        return max_length



class Solution2:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        # base cases
        if n < 2:
            return max(nums[0]-1, 0)
        s = sum(nums)
        if s > n -2:
            return n-1

        # create prefix and suffix array for storing contigous ones in the left and right of an index
        left_pre = [0]*n
        right_suf = [0]*n
        left_ptr, right_ptr = 1, n-2

        # update prefix and suffix array
        while left_ptr < n or right_ptr > -1:
            # prefix update
            temp_count = 0
            while left_ptr < n and nums[left_ptr-1] == 1:
                temp_count+=1
                left_pre[left_ptr] = temp_count
                left_ptr+=1
            if  left_ptr < n and nums[left_ptr-1] == 0 :
                left_pre[left_ptr] = 0
            left_ptr+=1

            # suffix update
            temp_count = 0
            while right_ptr > -1 and nums[right_ptr+1]==1:
                temp_count+=1
                right_suf[right_ptr] = temp_count
                right_ptr-=1
            if right_ptr > -1 and nums[right_ptr+1] == 0:
                right_suf[right_ptr] = 0
            right_ptr-=1
        
        # find element with maximum left and right ones
        max_count = 0
        for i in range(n):
            max_count = max(max_count, left_pre[i] + right_suf[i])
        return max_count

            
