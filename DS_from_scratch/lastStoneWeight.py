class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        # create max heap
        for stone in stones:
            heappush(max_heap, -1*stone)
        
        # while there are more than two stones
        while (len(max_heap) > 1):

            # get the heaviest stone
            heaviest_stone = -1*heappop(max_heap)

            # get the second heviest stone
            second_heaviest_stone = -1*heappop(max_heap)

            # smash them
            if heaviest_stone > second_heaviest_stone:
                heappush(max_heap, -1*(heaviest_stone - second_heaviest_stone))
        
        # return the remaining stone
        if max_heap:
            return -1*max_heap[0]
        return 0