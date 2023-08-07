class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # count num rows and cols
        numRows, numCols = len(grid), len(grid[0])
        count_fresh = 0
        queue = deque([])

        # possible movements in a grid i.e left, right, up and down
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] == 1:
                    count_fresh += 1
                elif grid[i][j] == 2:
                    queue.append([i,j])
        if count_fresh == 0:
            return 0
        
        # time variable for tracking minutes passed
        time = 0
        self.visited = set()
        while len(queue):
            for l in range(len(queue)):
                curr = queue.popleft()
                curr_x, curr_y = curr[0], curr[1]

                # check if all oranges are rotten
                if count_fresh == 0:
                    return time + 1
                
                for direction in directions:
                    temp_x, temp_y = curr_x + direction[0], curr_y + direction[1]
                    if (temp_x, temp_y) not in self.visited:

                        # check if the neighbour exist and can be visited
                        if temp_x > -1 and temp_x < numRows and temp_y > -1 and temp_y < numCols and grid[temp_x][temp_y] != 0:
                            queue.append([temp_x, temp_y])
                            self.visited.add((temp_x, temp_y))

                            # check if the orange is fresh, then rot it and reduce fresh orange by one
                            if grid[temp_x][temp_y] == 1:
                                count_fresh -= 1
                            
                            # check if all oranges are rotten
                            if count_fresh == 0:
                                return time + 1
            time += 1
            

        return -1