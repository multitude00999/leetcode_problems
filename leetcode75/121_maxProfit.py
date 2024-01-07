class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        p = 0
        while left < len(prices) and right < len(prices):
            if prices[right] > prices[left]:
                p = max(p, prices[right] - prices[left])
                right += 1
            
            else:
                left = right
                right += 1
        return p