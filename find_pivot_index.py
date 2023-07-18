class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum = 0
        n = len(nums)
        s = sum(nums)
        rsum = s - lsum - nums[0]
        if rsum == lsum:
            return 0
        for i in range(1, n):
            lsum += nums[i-1]
            rsum = s - lsum - nums[i]
            if rsum == lsum:
                return i

        return -1