class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n<2:
            return
        ptr1, ptr2 = 0, 1
        while ptr1 < n and ptr2 < n:
            # iterate until a zero element is found
            while ptr1 < n and nums[ptr1]!=0:
                ptr1+=1

            # find the closest non zero element 
            ptr2 = ptr1 + 1
            while ptr2 < n and nums[ptr2]==0:
                ptr2+=1
            
            # check break condition
            if ptr1 > n-1 or ptr2 > n-1:
                return
            # swap the non zero and zero value
            nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
            ptr1+=1
            ptr2+=1