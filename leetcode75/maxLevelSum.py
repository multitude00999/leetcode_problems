class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        # perform breadth first search
        queue = deque([root])
        global_max = -float('inf')
        level_counter = 1
        ans_level = 1

        while len(queue):
            level_size = len(queue)

            # calculate sum for current level
            temp = 0
            for i in range(level_size):
                curr = queue.popleft()
                temp += curr.val

                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)
            # check if current level is the max
            if global_max < temp:
                global_max = temp
                ans_level = level_counter
            level_counter += 1
        return ans_level