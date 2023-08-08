class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # create two minheaps for both ends
        minHeap1, minHeap2 = costs[:candidates], costs[max(candidates, len(costs)-candidates):]
        heapify(minHeap1)
        heapify(minHeap2)
        
        
        n = len(costs)
        # two pointer for tracking next element for each heap
        left, right = candidates, n - 1 - candidates
        ans = 0
        count = 0
        while count < k:
            # check if minHeap2 is empty or minHeap1 exist and minimum of minHeap1 is smaller than minheap2
            if not minHeap2 or minHeap1 and minHeap1[0] <= minHeap2[0]:
                ans += heappop(minHeap1)

                # push new element until curr lenght of array < candidates
                if left <=right:
                    heappush(minHeap1, costs[left])
                    left += 1
            
            else:
                ans += heappop(minHeap2)
                # push new element until curr lenght of array < candidates
                if left <= right:
                    heappush(minHeap2, costs[right])
                    right -= 1
            count += 1

        return ans