class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        val1, val2, val3 = float('inf'), float('inf'), float('inf')
        for i in range(n):
            if nums[i] <= val1:
                val1 = nums[i]
            elif nums[i] <= val2:
                val2 = nums[i]
            elif nums[i] <= val3:
                val3 = nums[i]
                return True
        return False