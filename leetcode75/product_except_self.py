class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        cnt_z = 0
        n = len(nums)

        # calculate product of array ignoring zeroes
        for i in range(n):
            if nums[i]==0:
                cnt_z+=1
            else:
                prod *= nums[i]
        
        # do inplace replacement for prod in the array
        for i in range(n):
            if cnt_z>1:
                nums[i]=0
                continue
            elif cnt_z == 1:
                if nums[i]!=0:
                    nums[i]= 0
                else:
                    nums[i]=prod

            else:
                nums[i] = prod//nums[i]

        return nums
