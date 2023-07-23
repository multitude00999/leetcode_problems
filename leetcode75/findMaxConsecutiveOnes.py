class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        temp_count, max_count = 0, 0
        while i < n:
            temp_count = 0

            # increment count until consecutive element is 1
            while i < n and nums[i] == 1:
                temp_count+=1
                i+=1
            
            # update maximum count
            max_count = max(max_count, temp_count)
            i+=1
        return max_count