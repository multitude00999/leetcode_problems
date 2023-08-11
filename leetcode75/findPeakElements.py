class Solution:
    def findPeakElementUtil(self, nums: List[int], low: int, high: int):
        # break condition
        if not low <= high:
            return -1

        # check mid is peak
        mid = (low + high)//2
        if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
            return mid
        
        # check on left half
        a = self.findPeakElementUtil(nums, low, mid - 1)
        if a != -1:
            return a

        # if peak not on left half check right half
        b = self.findPeakElementUtil(nums, mid + 1, high)
        if b != -1:
            return b
        return -1


    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        # base cases
        if n < 2:
            return 0
        if n < 3:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1

        # check boundary cases
        low, high = 0, len(nums) - 1
        if nums[low] > nums[low+1]:
            return low
        if nums[high] > nums[high - 1]:
            return high
        low += 1
        high -=1
        # check for element on the remaining array (excluding first and last element)
        return self.findPeakElementUtil(nums, low, high)
        
