class Solution:
    def dfs(self, root: int, n: int):
        # visit the node
        self.visited[root] = 1
        for neighbour in self.adjList[root]:
            # check neighbour ot visited
            if not self.visited[neighbour[0]]:
                # check if the edge is forward i.e. from root to neighbour
                if neighbour[1] == 1:
                    self.count += 1
                self.dfs(neighbour[0], n)
        
        return 

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.adjList = [[]for _ in range(n)]
        self.visited = defaultdict(int)
        self.count = 0

        # treat graph is undirected and count number of forward edges
        # create adjacency list with a flag for each representing whether edge is forward or not
        for c in connections:
            self.adjList[c[0]].append([c[1], 1])
            self.adjList[c[1]].append([c[0], 0])

        # run dfs
        self.dfs(0, n)
        return self.count