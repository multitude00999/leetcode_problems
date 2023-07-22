class Solution:
    def maxArea(self, height: List[int]) -> int:

        # intialize two pointer at each endo of the array
        n = len(height)
        left_ptr, right_ptr = 0, n - 1
        max_vol = -float('inf')
        while left_ptr < right_ptr:

            # calculate vol
            vol = (right_ptr - left_ptr)*(min(height[left_ptr] , height[right_ptr]))

            # update max vol
            max_vol = max(vol, max_vol)

            # move the smaller height pointer
            if height[left_ptr] < height[right_ptr]:
                left_ptr += 1
            elif height[left_ptr] >= height[right_ptr]:
                right_ptr -= 1
        return max_vol