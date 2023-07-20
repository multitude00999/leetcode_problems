class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref, suff, n = 1, 1, len(nums)
        res = [1]*n

        # using prefix and suffix 
        for i in range(n):
            res[i] *= pref
            pref *= nums[i]
            res[-1-i] *= suff
            suff*= nums[-1-i] 

        return res
