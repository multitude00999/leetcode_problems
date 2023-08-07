class Solution:
    def checkBoundary(self, x, y):
        # check if boundary reached
        return x == 0 or y == 0 or x == self.numRows - 1 or y == self.numCols - 1 
        
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        # count rows and columns
        self.numRows, self.numCols = len(maze), len(maze[0])
        
        # initialize visited set
        self.visited = set()

        # four possible directions
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        # current level counter
        level_counter = 0

        # add starting position to queue
        queue = deque([[entrance[0],  entrance[1]]])
        self.visited.add((entrance[0], entrance[1]))

        # perform BFS until boundary found
        while len(queue):

            # increase level only once done with all of the nodes at a particular level
            for l in range(len(queue)):
                curr = queue.popleft()
                curr_x, curr_y = curr[0], curr[1]
                # check if boundary found
                if level_counter > 0 and self.checkBoundary(curr_x, curr_y):
                    return level_counter
                
                # search neigbours of current node
                for direction in directions:
                    temp_x, temp_y = curr_x + direction[0], curr_y + direction[1]

                    # check if node exists and can be visited
                    if (temp_x, temp_y) not in self.visited and temp_x > -1 and temp_y > -1 and temp_x < self.numRows and temp_y < self.numCols and maze[temp_x][temp_y] != '+':

                        # check boundary condition
                        if self.checkBoundary(temp_x, temp_y):
                            return level_counter + 1
                        queue.append([temp_x, temp_y])
                        self.visited.add((temp_x, temp_y))
            level_counter += 1
            

        return -1
        