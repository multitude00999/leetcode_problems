class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashmap = {}
        n = len(nums)

        # make a hasmap storing count of each element
        for i in range(n):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
        pair_count = 0
        for i in range(n):
            if nums[i] in hashmap and k-nums[i] in  hashmap:

                # check if nums[i] and k-nums[i] are same
                if k-nums[i] == nums[i] and hashmap[k-nums[i]] < 2:
                    continue
                
                # increment pair count
                pair_count+=1

                # remove count of pair from hashmap
                hashmap[nums[i]] -= 1
                hashmap[k-nums[i]] -= 1
                if hashmap[nums[i]] < 1:
                    hashmap.pop(nums[i])
                if k - nums[i] in hashmap and hashmap[k - nums[i]] < 1:
                    hashmap.pop(k - nums[i])
        return pair_count