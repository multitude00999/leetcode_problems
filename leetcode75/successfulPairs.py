class Solution:
    def whereInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high)//2
            if nums[mid] < target:
                low = mid + 1
            
            else:
                high = mid
        return low
        
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        for s in spells:
            minPotion = ceil(success/s)

            # bisect left method
            index = self.whereInsert(potions, minPotion)
            ans.append(len(potions) - index)

        return ans
