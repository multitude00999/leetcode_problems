class dsu:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1 for _ in range(size)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    

    def union(self, x, y):
        x_par = self.find(x)
        y_par = self.find(y)

        if x_par!= y_par:

            if self.size[x_par] < self.size[y_par]:
                self.parent[x_par] = y_par
                self.size[y_par] += self.size[x_par]

            else:
                self.parent[y_par] = x_par
                self.size[x_par] += self.size[y_par]


    
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        uf = dsu(n)

        vis = dict()
        for i , num in enumerate(nums):
            if num in vis:
                continue
            
            vis[num] = i
            if num - 1 in vis:
                uf.union(i, vis[num-1])

            if num + 1 in vis:
                uf.union(i, vis[num + 1])

        return max(uf.size + [0])
            