class Solution:
    def returnPath(self, start, target, ans):
        # check if reached the target    
        if start == target:
            return ans
        
        # mark visited
        self.visited[start] = 1
        for neighbour in self.adjList[start]:
            if not self.visited[neighbour[0]]:
                a = self.returnPath(neighbour[0], target, ans*neighbour[1])
                # if target node found
                if a !=-1:
                    return a
        # if not found
        return -1
    
    def resetVisited(self):
        # reset the visited matrix after each query evaluation
        for key in self.visited.keys():
            self.visited[key] = 0
        return

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # intialize adJancency list and visited matrix
        self.adjList = defaultdict(list)
        self.visited = {}

        # create graph
        numEq = len(equations)
        for i in range(numEq):
            self.adjList[equations[i][0]].append([equations[i][1], values[i]])
            self.adjList[equations[i][1]].append([equations[i][0], 1/values[i]])
            self.visited[equations[i][0]] = 0
            self.visited[equations[i][1]] = 0
        
        # evaluate queries
        res = []
        for q in queries:
            # check if the queris exist
            if q[0] not in self.visited.keys() or q[1] not in self.visited.keys():
                res.append(-1)
                continue
    
            ans = self.returnPath(q[0], q[1], 1)
            res.append(ans)

            # unvisit the nodes
            self.resetVisited()
    
        return res
            

        