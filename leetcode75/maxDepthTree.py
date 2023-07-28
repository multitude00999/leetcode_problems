class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case
        if root == None:
            return 0
        
        # return maximum of depth of left subtree and right subtree + 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1