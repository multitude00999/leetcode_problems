class Solution:
    def check(self, h: int, possAns: int) -> bool:
        # function to chech if eating at possAns rate koko will be able to finish within h hours
        sum = 0
        for p in self.piles:
            sum += ceil(p/possAns)
            if sum > h:
                return False
        return True
        

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles
        # search range
        low, high = 1, 1e9
        prev = -1

        # binary searhc for answer in this range
        while low <= high:
            mid = (low + high)//2
            if self.check(h, mid):
                prev = mid
                high = mid - 1
            
            else:
                low = mid + 1
        return int(prev)