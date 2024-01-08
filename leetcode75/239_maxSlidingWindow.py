class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        if k == 1:
            return nums
        
        # maintain a monotonic decreasing q
        q = deque()
        ans = []

        for i in range(len(nums)):
            while q and q[0] < i - k + 1:
                q.popleft()
            
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            
            q.append(i)
            if i >= k - 1:
                ans.append(nums[q[0]])

        return ans