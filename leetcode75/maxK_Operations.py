class Solution1:
    def maxOperationsHashMap(self, nums: List[int], k: int) -> int:
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


class Solution2:
    def maxOperations2PTR(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # sort array in increasing order
        nums.sort()

        # intialize two pointer at both of the ends of the array
        left_ptr, right_ptr = 0, n - 1
        pair_count = 0

        while left_ptr < right_ptr:

            # update left pointer if sum is smaller
            if nums[left_ptr] + nums[right_ptr] > k:
                right_ptr -= 1
            
            # update right pointer if sum is larger
            elif nums[left_ptr] + nums[right_ptr] < k:
                left_ptr += 1
            
            # update both when the sum is equal to k and increase answer count
            else:
                pair_count += 1
                left_ptr += 1
                right_ptr -= 1
        
        return pair_count