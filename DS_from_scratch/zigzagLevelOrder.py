class Solution:

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        queue = [root]
        ans = []
        level = 1

        # loop over various levels
        while len(queue):
            size = len(queue)
            level_vals = []
            for i in range(size):
                curr = queue.pop(0)
                level_vals.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            # reverse the node values it if the level is even
            if level%2 == 0:
                level_vals = level_vals[::-1]
            ans.append(level_vals)
            level+=1
        return ans