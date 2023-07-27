class RecentCounter:

    def __init__(self):
        self.recentRequestCount = 0
        self.queue = []
        

    def ping(self, t: int) -> int:

        # base case
        if len(self.queue) == 0:
            self.queue.append(t)
            return 1
        
        self.queue.append(t)

        # keep deleting elements that are out of range [t-3000, t]
        while len(self.queue) and self.queue[0] < t  - 3000:
            self.queue.pop(0)
        
        # return size of queue
        return len(self.queue)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)