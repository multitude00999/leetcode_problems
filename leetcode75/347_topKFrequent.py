class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # store count in hashmap
        hashmap = defaultdict(int)
        for n in nums:
            hashmap[n] += 1

        # use bucket sort where key is number of occurences of the number
        n = len(nums)
        bsort_list = [[] for _ in range(n+1)]
        for key in hashmap.keys():
            bsort_list[hashmap[key]].append(key)

        # get k most frequent
        count = 0
        i = n
        ans = []
        while count < k and i > -1 :
            if len(bsort_list[i]) > 0:
                j = 0
                while count < k and j < len(bsort_list[i]):
                    ans.append(bsort_list[i][j])
                    count += 1
                    j +=1 
            i -= 1

        return ans
