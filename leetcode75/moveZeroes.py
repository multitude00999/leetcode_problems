class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n<2:
            return
        ptr1 = 0
        for ptr2 in range(n):
            # checkif there is non zero number and zero number to be swapped
            if nums[ptr2]!=0 and nums[ptr1] == 0:
                nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
            
            # check for zero value for pointer 1
            if nums[ptr1]!=0:
                ptr1+=1