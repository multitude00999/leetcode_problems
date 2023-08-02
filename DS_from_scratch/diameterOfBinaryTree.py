class Solution:
    def calcDepth(self, root: Optional[TreeNode]):

        # base case
        if root == None:
            return 0
        
        # calculate depth of left and  right subtree
        ld = self.calcDepth(root.left)
        rd = self.calcDepth(root.right)

        # update max diameter
        self.ans = max(self.ans, ld + rd)
        return max(ld, rd) + 1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.calcDepth(root)

        return self.ans