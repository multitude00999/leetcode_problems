class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:

        # sort nums 1 array by nums 2 array in decreasing order
        paired_arr = list(zip(nums1, nums2))
        paired_arr.sort(key = lambda x: x[1], reverse = True)
        n = len(paired_arr)

        # calculate score by considering each element of nums2 array one by one and taking max over it
        minHeap = []
        currSum, ans = 0, 0
        for i in range(k):
            heappush(minHeap, paired_arr[i][0])
            currSum += paired_arr[i][0]
        res = currSum*paired_arr[k-1][1]

        for i in range(k, n):
            currSum -= heappop(minHeap)
            currSum += paired_arr[i][0]
            res = max(res, currSum*paired_arr[i][1])
            heappush(minHeap, paired_arr[i][0])
        return res
