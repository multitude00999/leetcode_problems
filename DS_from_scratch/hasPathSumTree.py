class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False

        # check if leaf node
        if not root.left and not root.right:
            return targetSum - root.val == 0

        # check if left subtree or right subtree have a path where pathSum = targetSum
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)