# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLeaf(self, root: Optional[TreeNode]) -> List[int]:
        # base cases
        if root == None:
            return []
        
        #check if leaf node
        if root.left == None and root.right == None:
            return [root.val]
        
        # check leaves for left and right subtree
        return self.getLeaf(root.left) + self.getLeaf(root.right)
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        # compare leaves of left and right subtree
        l1 = self.getLeaf(root1)
        l2 = self.getLeaf(root2)

        if l1 == l2:
            return True
        return False