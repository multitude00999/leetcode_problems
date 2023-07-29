# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def height(self, root: Optional[TreeNode]) -> int:
#         # calculate height of tree
#         if root == None:
#             return 0

#         # calculate maximum of left and right subtree height + 1
#         return max(self.height(root.left), self.height(root.right)) + 1

#     def getCurrLevel(self, root: Optional[TreeNode], level: int) -> List[int]:

#         # print current level
#         if root == None:
#             return []

#         if level == 1:
#             return [root.val]
#         return self.getCurrLevel(root.left, level -1) + self.getCurrLevel(root.right, level -1)

#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if root == None:
#             return []
#         max_height = self.height(root)
#         ans = []

#         # loop over various levels
#         for i in range(1, max_height+1):
#             ans.append(self.getCurrLevel(root, i))
#         return ans

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        queue = deque([root])
        ans = []

        # loop over various levels
        while len(queue):
            size = len(queue)
            level_vals = []
            for i in range(size):
                curr = queue.popleft()
                level_vals.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            ans.append(level_vals)
        return ans

            
            
        

        