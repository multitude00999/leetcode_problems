class Solution:
    def sortedTwoSum(self, nums, lind, rind, target):
        ans = []
        while lind < rind:
            if nums[lind] + nums[rind] < target:
                lind += 1
            elif nums[lind] + nums[rind] > target:
                rind -= 1
            else:
                ans.append([lind, rind])
                lind += 1
                rind -= 1
                while lind < rind and nums[lind-1] == nums[lind]:
                    lind += 1
                while lind < rind and nums[rind+1] == nums[rind]:
                    rind -= 1
        return ans
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        i = 0
        ans = []
        while i < n - 2:
            temp = self.sortedTwoSum(nums, i + 1, n - 1, -nums[i])
            if len(temp):
                for j in range(len(temp)):
                    ans.append([nums[i], nums[temp[j][0]], nums[temp[j][1]]])
            i+=1
            while i < n - 2 and nums[i-1] == nums[i]:
                i+=1
            
        return ans

