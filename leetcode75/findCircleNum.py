class Solution:
    def dfs(self, isConnected: List[List[int]], curr: int):
        # dfs over current node
        self.visited[curr] = 1
        for i in range(self.numNodes):
            if isConnected[curr][i] and not self.visited[i]:
                self.dfs(isConnected, i)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.numNodes = len(isConnected)
        self.visited = defaultdict(int)
        self.connectedComponents = 0

        # perform dfs over each of the non visited node, and increase counter
        for i in range(self.numNodes):
            if not self.visited[i]:
                self.dfs(isConnected, i)
                self.connectedComponents +=1 

        return self.connectedComponents