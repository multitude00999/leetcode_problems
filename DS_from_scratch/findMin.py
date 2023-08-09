class Solution:
    def findMin(self, nums: List[int]) -> int:
        # base case 1: n rotations or array of length 1
        if nums[0] <= nums[-1]:
            return nums[0]
        
        # base case 2: n-1 rotations
        if nums[-1] < nums[-2]:
            return nums[-1]
        
        # binary search for a point where elements on both sides are smaller
        left, right = 0, len(nums) - 1

        while left < right:
            
            # mid
            mid = (left + right)//2

            # check if mid is the minimum
            if nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
                left = right = mid
                return nums[mid]
            
            # check if minimum is on left
            elif nums[left] > nums[mid]:
                right = mid
            
            # minimum is on right
            else:
                left = mid