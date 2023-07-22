class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        # calculate sum of first k sized array 
        temp_sum = sum(nums[:k])
        max_sum = temp_sum

        for i in range(1, n-k+1):

            # update subarray by removing leftmost element and adding right most element
            temp_sum += nums[i+k-1] - nums[i-1]

            # update max sum
            max_sum = max(max_sum, temp_sum)
            
        # calculate max average
        max_avg = max_sum/k
        return max_avg