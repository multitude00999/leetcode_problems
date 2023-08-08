class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.minHeap = []
        

    def popSmallest(self) -> int:
        if len(self.minHeap):
            ans = heappop(self.minHeap)
            return ans
        else:
            ans = self.smallest
            self.smallest += 1
            return ans

    def addBack(self, num: int) -> None:
        if not num >= self.smallest and num not in self.minHeap:
            heappush(self.minHeap, num)