class Solution1:
    def dfs(self, rooms: List[List[int]], curr: int) -> bool:

        # visit current node
        self.visited[curr] = 1

        # increase visited count
        self.count += 1

        # traverse not visited neighbours
        for neighbour in rooms[curr]:
            if not self.visited[neighbour]:
                self.dfs(rooms, neighbour)
        
        # check if all visited
        if self.count == self.numRooms:
            return True
        return False

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.count = 0
        self.numRooms = len(rooms)

        # initialize every nodeas not visited
        self.visited = defaultdict(int)

        return self.dfs(rooms, 0)

class Solution2:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.count = 0
        self.numRooms = len(rooms)

        # initialize every nodes not visited
        self.visited = defaultdict(int)

        # bfs over graph
        queue = deque([0])
        self.visited[0] = 1
        self.count += 1
        while len(queue):
            curr = queue.popleft()
            for neighbour in rooms[curr]:
                if not self.visited[neighbour]:
                    queue.append(neighbour)
                    self.visited[neighbour] = 1
                    self.count += 1

        if self.count == self.numRooms:
            return True

        return False