class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # base cases
        if n < 2:
            return min(k,1)

        # initialize two pointers at the starting of the array
        left_ptr, right_ptr, num_zeroes = 0, 0, 0
        max_length, curr_length = 0, 0

        # move right pointer for iterating over the array
        for right_ptr in range(n):
            if nums[right_ptr] == 0:
                num_zeroes += 1
            
            # move left pointer until there is only one zero in the subarray
            while left_ptr < n and num_zeroes > k:
                if nums[left_ptr] == 0:
                    num_zeroes -= 1
                left_ptr += 1
            curr_length = right_ptr - left_ptr + 1
            max_length = max(max_length, curr_length)

        return max_length