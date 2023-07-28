class Solution:
    def calculateGoodNodes(self, root: TreeNode, currmax: int) -> int:
        # utility for checking good nodes in left and right subtree

        # base case
        if root == None:
            return 0
        count = 0
        # compare root node with curr max
        if root.val >= currmax:
            currmax = root.val
            count += 1
        
        return count + self.calculateGoodNodes(root.left, currmax) + self.calculateGoodNodes(root.right, currmax)
    
    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        # update curr max
        currmax = root.val

        # check left and right subtree
        return 1 + self.calculateGoodNodes(root.left, currmax) + self.calculateGoodNodes(root.right, currmax)