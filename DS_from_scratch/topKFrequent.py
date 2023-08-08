class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for n in nums:
            hashmap[n] += 1
        
        maxHeap = []
        for i in hashmap.keys():
            heappush(maxHeap, (-hashmap[i], i))
        
        ans = []
        count = 0
        while count < k:
            ans.append(heappop(maxHeap)[1])
            count += 1
        return ans