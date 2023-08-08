class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = nums
        heapify(nums)

        # keep popping until min heap has length k
        while len(minHeap) > k:
            heappop(minHeap)
        return minHeap[0]